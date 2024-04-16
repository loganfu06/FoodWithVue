<template>
    <p>Vue is working</p>
  </template>
  <script>
  export default {
    name: 'App',
    components: {},
    data: function () {
      return {
        csrf_token: ext_csrf_token,
        form: ext_form,
        total_price: ext_total_price,
        customer: ext_customer,
        submitting_form: false,
        order_dico: ext_order_dico,
        food_list: ext_food_list
      }
    },
    methods: {
      
    },
    computed: {}
  }
  </script>