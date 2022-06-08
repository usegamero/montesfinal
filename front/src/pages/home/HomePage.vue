<template>
  <div class="container-image">
    <div class="container-text">
      <h1>MONTES DE LA PENÍNSULA IBÉRICA</h1>
    </div>
  </div>
</template>
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}
h1 {
  font-size: 50px;
}
.container-image {
  background-image: url(https://mott.pe/noticias/wp-content/uploads/2019/03/los-50-paisajes-maravillosos-del-mundo-para-tomar-fotos-1280x720.jpg);
  background-color: #cccccc;
  height: 500px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
.container-text {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
</style>