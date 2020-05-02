import React, { Component } from 'react';

class App extends Component {
  state = {
    saints: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/saintDay/saints/?format=json');
      const saints = await res.json();
      this.setState({
        saints
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.saints.map(item => (
          <div key={item.id}>
            <h1>{item.name}</h1>
            <h2>{item.country}</h2>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;