import ChatBox from './components/ChatBox'
import Controls from './components/Controls'

function App() {
  return (
    <div className="App">
      <h1 style={{ textAlign: "center", color: "#fff", marginTop: "2rem" }}>
        SerenityAI 🧘
      </h1>
      <ChatBox />
      {/* <Controls /> */}
    </div>
  )
}

export default App;
