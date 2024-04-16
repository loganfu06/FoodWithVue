import './assets/main.css'

import { createApp } from "vue";
import App from './App.vue';

import Multiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.min.css'

const app = createApp(App);

app.component('multiselect', Multiselect)

app.mount('#app');