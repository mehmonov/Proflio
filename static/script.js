function app() {
  return {
    step: 1,
    hasExperience: false,
    experiences: [
      {
        company: "",
        job_description: "",
        start_date: "",
        end_date: "",
        currently_working: false,
      },
    ],
    addExperience() {
      this.experiences.push({
        company: "",
        job_description: "",
        start_date: "",
        end_date: "",
        currently_working: false,
      });
    },
    async submitForm() {
      console.log("submitform word");
      
      const formData = {
        fullname: document.querySelector("#fullname").value,
        email: document.querySelector('#email').value,
        profession: document.querySelector('#profession').value,
        description: document.querySelector('#description').value,
        experiences: this.experiences
      };
      console.log(formData);
      
      function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
      }
      try {
        let csrftoken = getCookie('csrftoken');
        const response = await fetch('/mstep', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
          },
          body: JSON.stringify(formData),
        });

        if (response.ok) {
          this.step = 'complete';
          console.log(response);
          
        } else {
          console.error('Serverda xato: ', response.statusText);
        }
      } catch (error) {
        console.error('Tarmoq xatosi: ', error);
      }
    },
  };
}
