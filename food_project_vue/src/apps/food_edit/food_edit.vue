<template>
    hi

    <button type="+submit" class="btn btn-primary" @click.prevent="submit_form" :disabled="submitting_form">
        Submit
    </button>
</template>
<script>
export default {
    name: 'App',
    components: {
    },
    data: function () {
        return {
            csrf_token: ext_csrf_token,
            form: ext_form,
            food_price: ext_price,
            food_name: ext_name,
        }
    },
    methods: {
        submit_form() {
            if (this.submitting_form === true) {
                return;
            }
            this.submitting_form = true
            var form = document.createElement('form');
            form.setAttribute('method', 'post');
            let form_data = {
                'csrfmiddlewaretoken': this.csrf_token,
                'name': this.food_name,
                'price': this.food_price,
            }
            for (var key in form_data) {
                var html_field = document.createElement('input')
                html_field.setAttribute('type', 'hidden')
                html_field.setAttribute('name', key)
                html_field.setAttribute('value', form_data[key])
                form.appendChild(html_field)
            }
            document.body.appendChild(form);
            form.submit()
        },
    },
    computed: {
    }
}
</script>
