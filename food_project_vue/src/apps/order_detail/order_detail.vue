<template>
  <div>
    <a :href="this.order_list_url">order list</a><br /><br />
    <a :href="this.order_update_url">Update order</a><br />
    <a :href="this.order_delete_url">Delete order</a><br />
    <h1>{{ this.order.customer }}</h1>
    <h1>{{ this.order.total_price }}</h1>
    <li v-for="item in food">{{ item.name }} - ${{ item.price }}</li>
  </div>
</template>
<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
      order: ext_order_dico,
      food: ext_order_dico.food,
      id: ext_id,
      order_list_url: ext_order_list_url,
      order_update_url: ext_order_update_url,
      order_delete_url: ext_order_delete_url
    }
  },
  methods: {
    get_order_info() {
      fetch(this.order_detail_js_url, {
        method: 'get',
        credentials: 'same-origin'
      })
        .then(function (response) {
          console.log('response', response)
          return response.json()
        })
        .then(this.assign_order)
        .catch((error) => {
          console.log('error', error)
          this.order_error = ['error when loading order information']
        })
    },
    assign_order(order_json) {
      console.log('json', order_json)
      this.order = order_json['order']
    }
  },
  computed: {},
  beforeMount() {
    this.get_order_info()
  }
}
</script>
