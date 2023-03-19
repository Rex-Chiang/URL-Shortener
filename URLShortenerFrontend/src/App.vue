<template>
  <div id="app">
    <div align="center">
      <img src="./assets/logo.png" width="150" height="150">
      <router-view/>
    </div>
    <div>
      <b-container>
        <b-form @submit="shortenURL">
          <div align="center">
            <div align="center">
              <b-form-input id="long_url" v-model="long_url" type="text" placeholder="Please enter your URL" style="width:500px;" required>
              </b-form-input><br>
            </div>
            <b-btn type="submit">Shorten URL</b-btn>
          </div>
        </b-form>
      </b-container><br>
      <div align="center">
        <h5><strong> Short URL : </strong><small><i>{{ this.short_url }}</i></small></h5>
      </div>
    </div><br><br><br>
    <div>
      <mdb-footer color="mdb-color" class="font-small pt-4 mt-4">
        <div class="footer-copyright text-center">
          <mdb-container fluid>
            <i><h6><strong>&emsp;&emsp;&emsp;&emsp;&copy; 2022 Copyright: <a href="mailto:m41045@gmail.com"> Rex-Chiang </a></strong></h6></i>
          </mdb-container>
        </div>
      </mdb-footer>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  name: 'App',
  data () {
    return {
      long_url: '',
      short_url: ''
    }
  },
  methods: {
    shortenURL () {
      var api = 'http://0.0.0.0:8000/api/shorten'
      var params = new URLSearchParams()
      var instance = Axios.create({ validateStatus: function (status) { return status < 400 } })
      params.append('long_url', this.long_url)
      instance.post(api, params)
        .then((Response) => { console.log(Response.data); this.short_url = 'http://0.0.0.0:8000/' + Response.data.short_url })
        .catch((error) => { console.log(error); alert(error) })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
