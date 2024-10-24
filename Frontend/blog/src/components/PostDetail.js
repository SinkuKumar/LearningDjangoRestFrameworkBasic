import React, { useContext } from "react";
import { useParams } from "react-router-dom";
import { BlogContext } from "../context/BlogContext";

const PostDetail = () => {
  const { id } = useParams();
  const { posts, loading } = useContext(BlogContext);

  if (loading) return <div>Loading...</div>;

  const post = posts.find((post) => post.id === parseInt(id));

  if (!post) return <div>Post not found</div>;

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </div>
  );
};

export default PostDetail;
