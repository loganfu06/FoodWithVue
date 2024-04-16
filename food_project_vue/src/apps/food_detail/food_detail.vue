<template>
  <div>
    <a href="/food">Food list</a><br /><br />
    <a href="#">Update Food</a><br />
    <a href="#">Delete Food</a><br />
    <h1>{{ food_name }}</h1>
    <h1>{{ food_price }}</h1>
  </div>
</template>
<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
      food_price: ext_price,
      food_name: ext_name,
      food_id: ext_id
    }
  },
  methods: {},
  computed: {}
}
</script>
