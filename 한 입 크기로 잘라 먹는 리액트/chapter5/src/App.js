import "./App.css";
import Header from "./component/Header";
import Body from "./component/Body";
import Footer from "./component/Footer";

function App() {
  const BodyProps = {
    name: "칼코",
    location: "대한민국",
    // favorList: ["피자", "치킨", "떡볶이"],
  };
  return (
    <div className="App">
      <Header />
      <Body {...BodyProps} />
      <Footer />
    </div>
  );
}

export default App;
