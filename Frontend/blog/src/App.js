import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import PostList from "./components/PostList";
import PostDetail from "./components/PostDetail";
import PostForm from "./components/PostForm";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PostList />} />
        <Route path="/blogs/:id" element={<PostDetail />} />
        <Route path="/new-post" element={<PostForm />} />
      </Routes>
    </Router>
  );
};

export default App;
