<template>
  <div>
    <Header></Header>
    <Banner></Banner>
    <Footer></Footer>
  </div>
</template>

<script>


import Banner from "@/views/Banner";
import Header from "@/components/Header";
import Footer from "@/components/Footer";


export default {
  name: "Home",
  components: {
    Header: Header,
    Footer: Footer,
    Banner: Banner,
  }
}
</script>

<style scoped>

</style>