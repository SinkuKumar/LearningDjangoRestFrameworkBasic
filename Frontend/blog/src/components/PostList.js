import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const PostList = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/blogs/?format=json")
      .then((response) => setPosts(response.data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h1>Blog Posts</h1>
      <ul>
        {console.log(posts)}
        {posts.map((post) => (
          <li key={post.id}>
            <Link to={`/blogs/${post.id}?format=json`}>{post.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PostList;
