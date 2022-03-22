<template>
   <h1>montañas</h1> 
   <p>{{Monte}}</p>
   <button @click="AddLista">montes</button>
</template>
<script>
export default{
    data(){
        return{
            Monte:[]
                
            

        }
    },
    methods:{
        AddLista(){
            alert("soy dios")
        }

    }
}

</script>
<style>

</style>
