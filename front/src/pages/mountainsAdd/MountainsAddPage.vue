<template>
  <h1>New Mountain</h1>
  <form>
    <section class="form-data">
      <p>Nombre de la montaña</p>
      <input type="text" id="name" v-model="mountain.name" />
      <p>Altura de la montaña</p>
      <input type="text" id="name" v-model="mountain.height" />
      <p>Ciudad</p>
      <input type="text" id="name" v-model="mountain.city" />
      <p>Foto de la montaña</p>
      <input type="text" id="name" v-model="mountain.img" />
      <p>Localizacion de la montaña</p>
      <input type="text" id="name" v-model="mountain.location" />
      {{ mountain }}
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
</style>
