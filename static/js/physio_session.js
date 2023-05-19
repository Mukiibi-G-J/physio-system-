const resultsBoxPhysioSession = document.getElementById(
  "results-box-physio-session"
);
const search_input_physio_session = document.getElementById(
  "search_input_physio_session"
);
const PIN_NO = document.getElementById("pin_no");
const patient_id_1 = document.getElementById("patient_id");
const patient_name_1 = document.getElementById("patient_name");
const patient_surname_1 = document.getElementById("patient_surname");
const phone_1 = document.getElementById("phone");
const address_1 = document.getElementById("address");
const gender_1 = document.getElementById("gender");
const multiple_input_1 = document.getElementById("multiple_input");
const diagnosis_1 = document.getElementById("diagnosis")

function myFunctionPhysio(id) {
  resultsBoxPhysioSession.classList.add("d-none");

  console.log(id);
  $.ajax({
    type: "get",
    url: `get_patient_physio/${id}`,
    success: (response) => {
      //   console.log(response.data.visit_no);
      console.log(response.data);
      console.log(response.data);
      if (response.data) {
        patient_surname_1.innerHTML = `
              <label>Surname</label>
              <input class="form-control" name="patient_surname"  value=${response.data.surname} readonly id="surname"/>`;

        patient_name_1.innerHTML = `
              <label>First Name</label>
              <input class="form-control" name="firstname"  value=${response.data.firstname} readonly id="firstname"/>`;
        PIN_NO.innerHTML = `
              <label>PIN no</label>
              <input type="text" class="form-control" name="patient_pin" value=${response.data.pin_no} readonly id="patient_pin" />
              `;
        phone_1.innerHTML = `
          <label>phone no</label>
          <input type="text" class="form-control" name="phone" value=${response.data.phone} readonly id="phone" />
          `;
        gender_1.innerHTML = `
          <label>Gender</label>
          <input type="text" class="form-control" name="gender" value=${response.data.gender} readonly id="gender" />
          `;
          diagnosis_1.innerHTML=`
          <div style="margin-right:8px;">
            <label>Diagnosis</label>
            <input type="text" class="form-control" name="diagnosis" value=${response.data.diagnosis} readonly id="gender" />
          </div>  
          `;
      
          multiple_input_1.innerHTML = `
          <div style="margin-right:8px;">
          <label>Quantity of Sessions Paid for</label>
          <input type="text" class="form-control" name="quantity" value=${response.data.quantity} readonly />
          </div>        `;
      } else if (response.error) {
        iziToast.warning({
          title: `${response.error}`,

          position: "topRight",
        });
      }
    },
    error: (error) => {
      console.log(error);
      iziToast.warning({
        title: `${error.responseJSON.message}`,

        position: "topRight",
      });
    },
  });
}

const sendSearchDataPhysioSession = async (patient) => {
  $.ajax({
    type: "POST",
    url: "search/",
    data: {
      csrfmiddlewaretoken: crf,
      name: patient,
    },
    success: (response) => {
      console.log(response.data);
      if (Array.isArray(response.data)) {
        resultsBoxPhysioSession.innerHTML = "";
        response.data.forEach((patient) => {
          const pin_no = patient.pin_no.replace("P", "");

          resultsBoxPhysioSession.innerHTML += `<a href="/patient" class="item">
  
                        <div class="list-group">
                          
                        
                          
                            <a style="cursor:pointer;"   class="list-group-item list-group-item-action"  onClick="myFunctionPhysio(id=${pin_no})">${patient.pin_no}-${patient.surname}-${patient.name}</a>
                         
                        
  
                        
                    </div>
          
            </a>`;
        });
      } else {
        if (search_input_physio_session.value.length > 0) {
          resultsBoxPhysioSession.innerHTML = `<div class="list-group"><a href="#" class="list-group-item list-group-item-action">${response.data}</a></div>`;
        } else {
          resultsBoxPhysioSession.classList.add("d-none");
        }
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
};

search_input_physio_session.addEventListener("keyup", (e) => {
  if (e.target.value.length > 8) {
    console.log(e.target.value);
    if (resultsBoxPhysioSession.classList.contains("d-none")) {
      resultsBoxPhysioSession.classList.remove("d-none");
    }
    sendSearchDataPhysioSession(e.target.value);
  }
});
