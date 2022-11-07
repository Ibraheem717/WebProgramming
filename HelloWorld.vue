<script>
import { ref } from 'vue'


export default{
  data () {
    return {
      name: "Ibraheem's Site",
      Questions: [],
      form: [],
      send: [
        {old_text: ""},
        {question_text: 'one'},
        {date_pub: 'two'} 
      ]
    }
  },
  methods: {

    async fetchData () {
      let data = await fetch("http://127.0.0.1:8000/polls/api/questions", {method: "GET"})
      let response = await data.json()
      this.Questions = response.Question
    },

    test () {
    this.name = "this is bs"
    console.log(name)
    },

    async fetchForm () {
      let data = await fetch("http://127.0.0.1:8000/polls/api/questions", {
        method : 'POST',
        body :  JSON.stringify({
          question_text : this.send.question_text,
          date_pub : this.send.date_pub
        })
      })
      let response = await data.json()
      this.form = response
    },

    async editForm () {
      let data = await fetch("http://127.0.0.1:8000/polls/api/questions", {
        method : 'PUT',
        body :  JSON.stringify({
          old_text : this.send.old_text,
          question_text : this.send.question_text,
          date_pub : this.send.date_pub
        })
      })
      let response = await data.json()
      this.form = response
    },

    async deleteForm () {
      let data = await fetch("http://127.0.0.1:8000/polls/api/questions", {
        method : 'DELETE',
        body :  JSON.stringify({
          question_text : this.send.question_text,
        })
      })
      let response = await data.json()
      this.form = response
    },
  }

};

const count = ref(0) 
</script> 

<template class="container">
  <h1 class="col-14">{{ name }}</h1>

  <ul>
    <li v-for="item in Questions"> <span> {{ item['text'] }} </span>
      <ul>
        <li v-for="indi in item"> <span> {{ indi }} </span> </li>
      </ul> 
    </li>
  </ul>


  <div class="invisible">{{ fetchData() }}</div>

  <form @submit.prevent="fetchForm">
    <input v-model="send.question_text">
    <input type="datetime-local" v-model="send.date_pub">
    <button >wefe</button>
  </form>
  ernghrogerhgiuerhgiurehgiherighiuerghirh
  <form @submit.prevent="editForm">
    <input v-model="send.old_text">
    <input v-model="send.question_text">
    <input type="datetime-local" v-model="send.date_pub">
    <button >Edit</button>
  </form>

  ernghrogerhgiuerhgiurehgiherighiuerghirh
  <form @submit.prevent="deleteForm">
    <input v-model="send.question_text">
    <button >Delete</button>
  </form>

</template>

