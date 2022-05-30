<template>
  <!-- <h1>Contact detail: {{ mountain.id }}</h1> -->
  <ul class="contact-item" >
    <li>Nombre: {{mountain.name}}</li>
    <li>Altura: {{ mountain.height }}</li>
    <li>Ciudad: {{ mountain.city }}</li>
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
        `${config.API_PATH}/mountains/${id}`,settings
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
  border: 2px solid dodgerblue;
  border-radius: 1em;
  padding: 1em;
  text-align: left;
}
</style>
