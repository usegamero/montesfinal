<template>
  <h1>New Mountain</h1>
  <form>
    <section class="form-data">
      <p>Nombre de la montaña</p>
      <input type="text" id="name" class="input " v-model="mountain.name" />
      <p>Altura de la montaña</p>
      <input type="text" id="name" class="input" v-model="mountain.height" />
      <p>Ciudad</p>
      <input type="text" id="name" class="input" v-model="mountain.city" />
      <p>Foto de la montaña</p>
      <input type="text" id="name" class="input" v-model="mountain.img" />
      <p>Localización de la montaña</p>
      <input type="text" id="name" class="input" v-model="mountain.location" />
      <p>Descripción de la montaña</p>
      <input
        type="text"
        id="name"
        class="input"
        v-model="mountain.description"
      />
    </section>
    <button @click.prevent="onSaveClicked">Guardar</button>
  </form>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import config from "@/config.js";

export default {
  name: "MountainsAddPage",
  data() {
    return {
      mountain: {
        name: "",
        id: "",
        height: "",
        city: "",
        img: "",
        location: "",
      },
      nombre: "Iker",
    };
  },
  methods: {
    async onSaveClicked() {
      this.mountain.id = uuidv4();
      const settings = {
        method: "POST",
        body: JSON.stringify(this.mountain),
        headers: {
          "Content-Type": "application/json",
        },
      };

      await fetch(`${config.API_PATH}/mountains`, settings);
      console.log("onSaveClicked", JSON.stringify(this.mountain));

      // const response = await fetch("http://localhost:5000/api/mountains");
      // this.mountains = await response.json();
    },
  },
};
</script>

<style scoped>
h1 {
  font-style: italic;
}
.form-data {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 1em 0;
}
button {
  text-decoration: none;
  position: absolute;
  border: none;
  font-size: 14px;
  font-family: inherit;
  color: #fff;
  width: 9em;
  height: 3em;
  line-height: 2em;
  text-align: center;
  background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
  background-size: 300%;
  border-radius: 30px;
  z-index: 1;
}

button:hover {
  animation: ani 8s linear infinite;
  border: none;
}

@keyframes ani {
  0% {
    background-position: 0%;
  }

  100% {
    background-position: 400%;
  }
}

button:before {
  content: "";
  position: absolute;
  top: -5px;
  left: -5px;
  right: -5px;
  bottom: -5px;
  z-index: -1;
  background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
  background-size: 400%;
  border-radius: 35px;
  transition: 1s;
}

button:hover::before {
  filter: blur(20px);
}

button:active {
  background: linear-gradient(32deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
}
.input {
  border: 3px solid rgb(127, 170, 170);
  border-radius: 20px;
  background-image: linear-gradient(120deg, #3c3c3c, #585858);
  color: rgb(127, 170, 170);
  cursor: pointer;
  padding: 7px 12px;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 17px;
  transition: all 1s;
  max-width: 170px;
  margin-bottom: 10px;
}



.input:focus {
  outline-color: rgb(127, 170, 170);
}
</style>
