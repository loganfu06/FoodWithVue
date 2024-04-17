<template>
  <form method="post" class="form">
    <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token" />
    <p>
      <label for="id_name">Customer name:</label>
      <input type="text" name="customer" v-model="customer" maxlength="100" required id="id_customer" />
    </p>
    <p>
      <label for="id_price">Total Price:</label> ${{ totalPrice }}
      <input type="hidden" name="total_price" v-model.number="total_price" required id="id_price" />
    </p>
    <p>
      <label for="id_food">Food:</label><br>
      <select hidden name="food" required="" id="id_food" multiple="">
        <option v-for="food in order_food_list" :value="food.id" selected=""></option>
      </select>
      <multiselect v-model="order_food_list" :options="food_source" track-by="id" label="name" :multiple="true">
      </multiselect>
      <li v-for="item in order_food_list">
        {{ item.name }} - ${{ item.price }}
      </li>
    </p>
  </form>
  <button type="submit" class="btn btn-primary" @click.prevent="submit_form" :disabled="submitting_form">
    Submit
  </button>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  name: 'App',
  components: {
    Multiselect,
  },
  data: function () {
    return {
      csrf_token: window.ext_csrf_token,
      form: window.ext_form,
      total_price: window.ext_total_price,
      customer: window.ext_customer,
      submitting_form: false,
      order_dico: window.ext_order_dico,
      food_source: window.ext_food_list,
      order_food_list: window.ext_order_dico.food,
    }
  },
  methods: {
    submit_form() {
      if (this.submitting_form === true) {
        return
      }
      this.submitting_form = true
      var form = document.createElement('form')
      form.setAttribute('method', 'post')
      let form_data = {
        csrfmiddlewaretoken: this.csrf_token,
        customer: this.customer,
        total_price: this.total_price,
      }
      for (var key in form_data) {
        var html_field = document.createElement('input')
        html_field.setAttribute('type', 'hidden')
        html_field.setAttribute('name', key)
        html_field.setAttribute('value', form_data[key])
        form.appendChild(html_field)
      }
      var food_field = document.createElement('select')
      food_field.setAttribute('name', 'food')
      food_field.setAttribute('id', 'id_food')
      food_field.setAttribute('multiple', '')
      for (var food of this.order_food_list) {
        var option_field = document.createElement('option')
        option_field.setAttribute('value', food.id)
        option_field.setAttribute('selected', '')
        food_field.appendChild(option_field)
      }
      form.appendChild(food_field)
      document.body.appendChild(form)
      form.submit()
    }
  },
  computed: {
    totalPrice() {
      let totalSum = 0
      for (var food in this.order_food_list) {
        let currentPrice = JSON.parse(JSON.stringify(this.order_food_list[food])).price
        console.log(currentPrice);
        totalSum += currentPrice
      }
      console.log(totalSum)
      this.total_price = totalSum
      return totalSum
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>