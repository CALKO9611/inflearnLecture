import "./Body.css";

function Body(props) {
  console.log(props);
  return (
    <div className="body">
      {props.name}는 {props.location}에 거주합니다
    </div>
  );
}

export default Body;
