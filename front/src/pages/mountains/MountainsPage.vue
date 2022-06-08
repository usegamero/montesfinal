<template>
  <h1>BUSCADOR DE MONTAÑAS</h1>
  <section>
    <article class="item" v-for="monte in montes" :key="monte.id">
      <button @click="openMountainDetail(monte)">Ver Detalle</button>
      <img :src="monte.img" alt="" srcset="" />
      <h2>
        {{ monte.name }}
      </h2>
      <!-- <router-link :to="`/contacts/${contact.id}`">ver detalle</router-link> -->
      <button @click="deleteMountain(monte)">Borrar Montaña</button>
    </article>
    <br />
    {{ montañadelocalstorage }}
  </section>
</template>
<script>
import config from "@/config.js";

export default {
  name: "MountainsPage",
  data() {
    return {
      montes: [],
      selectedMountain: null,
      montañadelocalstorage: {},
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const settings = {
        methods: "GET",
      };
      let response = await fetch(`${config.API_PATH}/mountains`, settings);
      let data = await response.json();
      console.log(data);
      this.montes = data;
      // console.log(data);
    },
    openMountainDetail(monte) {
      this.$router.push("/mountains/" + monte.id);
    },
    async deleteMountain(monte) {
      /*  const settings = {
        methods: "DELETE",
      }; */
      await fetch(`${config.API_PATH}/mountains/${monte.id}`, {
        method: "DELETE",
      });
      location.reload();
    },
  },
};
</script>

}
<!-- <style>
* {
  background-color: beige;
}
</style> -->
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
h1 {
  font-style: italic;
}
* {
  font-family: Poppins;
  font-weight: bold;
}

.contact-item {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
/* From uiverse.io by @kirzin */
button {
  text-decoration: none;
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
.item {
  display: flex;
  flex-direction: column;
  text-align: center;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  gap: 1rem;
  padding: 1rem;
  background: rgb(156, 19, 228);
  background: -moz-linear-gradient(
    125deg,
    rgba(156, 19, 228, 1) 0%,
    rgba(240, 45, 253, 1) 100%
  );
  background: -webkit-linear-gradient(
    125deg,
    rgba(156, 19, 228, 1) 0%,
    rgba(240, 45, 253, 1) 100%
  );
  background: linear-gradient(
    125deg,
    rgba(156, 19, 228, 1) 0%,
    rgba(240, 45, 253, 1) 100%
  );
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#9c13e4",endColorstr="#f02dfd",GradientType=1);
}
.item img {
  max-width: 20rem;
  border-radius: 50%;
}
section {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fill, min-max(15rem, 1fr));
}
</style>


