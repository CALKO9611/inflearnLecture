import React from "react";
import Comment from "./Comment";

const comments = [
  {
    name: "김서원",
    comment: "안녕하세요, 칼코입니다.",
  },
  {
    name: "유재석",
    comment: "리액트 재미있어요~!",
  },
  {
    name: "강민경",
    comment: "저도 리액트 배워보고 싶어요!!",
  },
];

function CommentList(props) {
  return (
    <div>
      {comments.map((user) => {
        return <Comment name={user.name} comment={user.comment} />;
      })}
    </div>
  );
}

export default CommentList;
