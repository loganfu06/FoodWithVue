<template>
  <div>
    <a :href="this.food_list_url">Food list</a><br /><br />
    <a :href="this.food_update_url">Update Food</a><br />
    <a :href="this.food_delete_url">Delete Food</a><br />
    <h1>{{this.food.name}}</h1>
    <h1>{{this.food.price}}</h1>
  </div>
</template>
<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
      food_id: ext_id,
      food_detail_js_url: ext_food_detail_js_url,
      food: "",
      food_list_url: ext_food_list_url,
      food_update_url: ext_food_update_url,
      food_delete_url: ext_food_delete_url,
    }
  },
  methods: {
    get_food_info() {
      fetch(this.food_detail_js_url,
        {
          method: "get",
          credentials: 'same-origin'
        }
      ).then(function (response) {
        console.log('response', response)
        return response.json()
      }).then(this.assign_food).catch(
        (error) => {
          console.log('error', error)
          this.food_error = ["error when loading food information"]
        })
    },
    assign_food(food_json) {
      console.log('json', food_json)
      this.food = food_json['food']
    },
  },
  computed: {},
  beforeMount() {
        this.get_food_info()
    },
}
</script>
