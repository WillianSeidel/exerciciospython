const express = require("express");

const createServer = (pool, port = 3000) => {
  const app = express();

  // Rota para obter os comentários de um post por ID
  app.get("/posts/:id/comments", async (req, res) => {
    const postId = parseInt(req.params.id, 10);

    try {
      // Obter todos os comentários e comentários filhos do post
      const result = await pool.query(
        `
        WITH RECURSIVE comment_tree AS (
          SELECT id, text, parent_id, post_id
          FROM comments
          WHERE post_id = $1 AND parent_id IS NULL
          UNION ALL
          SELECT c.id, c.text, c.parent_id, c.post_id
          FROM comments c
          INNER JOIN comment_tree ct ON ct.id = c.parent_id
        )
        SELECT id, text, parent_id, post_id
        FROM comment_tree
        ORDER BY parent_id, id;
        `,
        [postId]
      );

      // Estruturar os comentários hierarquicamente
      const comments = result.rows;

      const buildTree = (comments) => {
        const map = new Map();
        const roots = [];

        comments.forEach((comment) => {
          // Cria a estrutura do comentário sem o parent_id e post_id
          map.set(comment.id, { id: comment.id, text: comment.text, children: [] });
        });

        comments.forEach((comment) => {
          if (comment.parent_id === null) {
            // Comentário principal (sem pai) é adicionado às raízes
            roots.push(map.get(comment.id, comment.text));
          } else {
            // Comentário filho é adicionado ao comentário pai
            const parent = map.get(comment.parent_id);
            parent.children.push(map.get(comment.id));
          }
        });

        return roots;
      };

      // Montar a árvore de comentários
      const structuredComments = buildTree(comments);

      // Excluir os campos parent_id e post_id
      const cleanedComments = structuredComments.map((comment) => {
        // Remover parent_id e post_id de cada comentário
        const { parent_id, post_id, ...cleaned } = comment;

        // Se o comentário não tiver filhos, remover o campo "children"
        if (cleaned.children.length === 0) {
          delete cleaned.children;
        }

        return cleaned;
      });

      res.json({ data: cleanedComments });
    } catch (error) {
      console.error(error);
      res.status(500).send("Internal Server Error");
    }
  });

  // Iniciar o servidor na porta fornecida
  const server = app.listen(port, () =>
    console.log(`[server] listening on port ${port}`)
  );

  return {
    app,
    close: () => new Promise(resolve => {
      server.close(() => {
        resolve();
        console.log("[server] closed");
      })
    }),
  };
};

module.exports = { createServer };
