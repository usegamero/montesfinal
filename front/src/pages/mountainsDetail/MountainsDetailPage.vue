<template>
  <!-- <h1>Contact detail: {{ mountain.id }}</h1> -->
  <ul class="contact-item">
    <li><b> Nombre:</b> {{ mountain.name }}</li>
    <li><b> Altura:</b> {{ mountain.height }}</li>
    <li><b> Ciudad:</b> {{ mountain.city }}</li>
    <li><b> Localización:</b> {{ mountain.location }}</li>
    <li><b> Descripción:</b> {{ mountain.description }}</li>
  </ul>
</template>

<script>
import config from "@/config.js";
export default {
  name: "MountainsDetailPage",
  data() {
    return {
      mountain: {},
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const settings = {
        methods: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      };
      // const response = await fetch("http://localhost:5000/api/contacts");
      // this.contacts = await response.json();
      let id = this.$route.params.id;
      const response = await fetch(
        `${config.API_PATH}/mountains/${id}`,
        settings
      );
      this.mountain = await response.json();
    },
  },
};
</script>

<style scoped>
h1 {
  font-style: italic;
}
.contact-item {
  border: 5px solid dodgerblue;
  border-radius: 1em;
  padding: 1em;
  text-align: left;
  font-size: 30px ;
  color:rgb(69, 143, 19);
  background-color: rgba(147, 177, 82, 0.396);
}
li {
  list-style: none;
  
}
</style>
