<template>
  <form method="post" class="form">
    <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token" />
    <p>
      <label for="id_name">Food Name:</label>
      <input type="text" name="name" v-model="food_name" maxlength="100" required id="id_name" />
    </p>
    <p>
      <label for="id_price">Price:</label>
      <input type="number" name="price" v-model.number="food_price" required id="id_price" />
    </p>
  </form>
  <button
    type="+submit"
    class="btn btn-primary"
    @click.prevent="submit_form"
    :disabled="submitting_form"
  >
    Submit
  </button>
</template>
<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
      csrf_token: ext_csrf_token,
      form: ext_form,
      food_price: ext_price,
      food_name: ext_name,
      submitting_form: false
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
        name: this.food_name,
        price: this.food_price
      }
      for (var key in form_data) {
        var html_field = document.createElement('input')
        html_field.setAttribute('type', 'hidden')
        html_field.setAttribute('name', key)
        html_field.setAttribute('value', form_data[key])
        form.appendChild(html_field)
      }
      document.body.appendChild(form)
      form.submit()
    }
  },
  computed: {}
}
</script>
