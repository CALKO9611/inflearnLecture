function Body({ name, location, favorList = [] }) {
  console.log(name, location, favorList);
  return (
    <div className="body">
      {name}는 {location}에 거주합니다.
      <br />
      {favorList.length}개의 음식을 좋아합니다.
    </div>
  );
}

export default Body;
