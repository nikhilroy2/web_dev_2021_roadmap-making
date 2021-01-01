
import './App.css';

function App() {
  return (
    <div className="App">
      <h1> Hello React Js <Fun1 name="Nikhil Roy"/> </h1>
    </div>
  );
}

function Fun1(props){
  return (
    <>
    I am {props.name}
    </>
  )
}
export default App;
