const zmq = require("zeromq");
const json = require("json");

async function run() {
  const socket = new zmq.Reply();

  await socket.bind("tcp://*:5555");

  for await (const [msg] of socket) {
    const json_data = msg.toString();
    console.log("Received:", json_data);

    const data = JSON.parse(json_data);
    console.log("readyForCopying:", data.readyForCopying);
    console.log("JSON Data:", data.json_data);

    if (data.readyForCopying) {
      delete data.json_data.category;
      data.readyForCopying = false;
    }

    const response_json = JSON.stringify(data);
    socket.send(response_json);
  }
}

run();
