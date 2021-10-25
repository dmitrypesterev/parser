const VueApp = new Vue({
   el: "#app",
	data: {
        list: [],
        newEmojies: [],
        formActive: false,
        emojiContainer: "",
        groups: {
            basics: {
               "id":"12",
               "name":"basics",
               "titles":{
                  "russian":"основы"
               }
            },
            animals: {
               "id":"0",
               "name":"animals",
               "titles":{
                  "russian":"животные"
               }
            },
            food: {
               "id":"1",
               "name":"food",
               "titles":{
                  "russian":"еда"
               }
            },
            clothes: {
               "id":"2",
               "name":"clothes",
               "titles":{
                  "russian":"одежда"
               }
            },
            colors: {
               "id":"3",
               "name":"colors",
               "titles":{
                  "russian":"цвета"
               }
            },
            family: {
               "id":"4",
               "name":"family",
               "titles":{
                  "russian":"семья"
               }
            },
            house: {
               "id":"5",
               "name":"house",
               "titles":{
                  "russian":"дом"
               }
            },
            professions: {
               "id":"6",
               "name":"professions",
               "titles":{
                  "russian":"профессии"
               }
            },
            subjects: {
               "id":"7",
               "name":"subjects",
               "titles":{
                  "russian":"предметы"
               }
            },
            nature: {
               "id":"8",
               "name":"nature",
               "titles":{
                  "russian":"природа"
               }
            },
            sport: {
               "id":"9",
               "name":"sport",
               "titles":{
                  "russian":"спорт"
               }
            },
            medicine: {
               "id":"10",
               "name":"medicine",
               "titles":{
                  "russian":"медицина"
               }
            },
            business: {
               "id":"11",
               "name":"business",
               "titles":{
                  "russian":"бизнес"
               }
            },
            city: {
               "id":"13",
               "name":"city",
               "titles":{
                  "russian":"город"
               }
            },
            travel: {
               "id":"13",
               "name":"travel",
               "titles":{
                  "russian":"поездки"
               }
            },
            body: {
               "id":"13",
               "name":"body",
               "titles":{
                  "russian":"тело"
               }
            },
            verbs: {
               "id":"13",
               "name":"verbs",
               "titles":{
                  "russian":"глаголы"
               }
            }
        }     
    },   
    
    methods: {
		async get_list () {
			this.list = await eel.get_list()();
		},

      async get_app_list () {
         this.newEmojies = await eel.get_app_list()();
         console.log(this.newEmojies)
      },

      addEmoji (index) {
         this.newEmojies.push(this.list[index]);
         localStorage.setItem('emojies', JSON.stringify(this.newEmojies));

         setTimeout(function () {
               document.querySelector(".list2").scrollTop = document.querySelector(".list2").scrollHeight;
         }, 10);
      },

      removeEmoji (index) {
         this.newEmojies.splice(index,1);      
      },
      
      saveEmojies () {
         let emojiesString = JSON.stringify(this.newEmojies, null,'\t');
         localStorage.setItem('emojies', emojiesString);

         this.emojiContainer = emojiesString.trim();
         this.formActive = true;
      },

      async saveEmojiesInFile () {
         let emojiesString = JSON.stringify(this.newEmojies, null,'\t');
         this.emojiContainer = emojiesString.trim();

         await eel.save_emojies(this.emojiContainer)();
         this.formActive = false;
      },

      changeName (index, event) {
         this.newEmojies[index].translations["english"] = event.target.innerText;
      },

      changeTranslate (index, event) {
         this.newEmojies[index].translations["russian"] = event.target.innerText;
      },

      copy () {
         let emojiJSONText = this.$refs.emojiJSONText;
         emojiJSONText.select();
         document.execCommand("copy");

         this.formActive = !this.formActive;
      }
    },

    async created () {
      await this.get_list();  
      await this.get_app_list();

      if ( !localStorage.hasOwnProperty('emojies') ) {
         await this.get_app_list();

         localStorage.emojies = "[]";
      } else {
         this.newEmojies = JSON.parse(localStorage.getItem('emojies'));
      }
    }
})
