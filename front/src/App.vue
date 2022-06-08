<template>
  <div id="nav">
    <router-link to="/mountains">Montañas</router-link>|

    <router-link to="/">Home</router-link>|
    <router-link to="/mountains/add">Añadir monte</router-link>|
  </div>
  <router-view />
</template>

<script>
</script>
<style scoped>
#nav{
  font-size: 25px 
  ;
}
</style>