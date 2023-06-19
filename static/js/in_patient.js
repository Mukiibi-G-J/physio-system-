console.log("jkjlaksd");
const resultsBoxInpatient = document.getElementById("results-box-inpatient");
const searchInputInpatient = document.getElementById("search_input_inpatient");
const patient_id_inpatient = document.getElementById("patient_id");
const patient_name_inpatient = document.getElementById("patient_name");
const patient_surname_inpatient = document.getElementById("patient_surname");
const PIN_IN_PATIENT = document.getElementById("pin_no");
const receipt_no_in_patient = document.getElementById("receipt_no");
const patient_type_in_patient = document.getElementById("patient_type");
const date_of_birth_in_patient = document.getElementById("date_of_birth");
const phone_in_patient = document.getElementById("phone");
const address_in_patient = document.getElementById("address");
const gender_in_patient = document.getElementById("gender");

const multiple_input_inpatient = document.getElementById("multiple_input");

function myFunction_inpatient(id) {
  resultsBoxInpatient.classList.add("d-none");

  console.log(id);
  $.ajax({
    type: "get",
    url: `get_in_patient/${id}`,
    success: (response) => {
      console.log(response.data.admission_no);
      //   console.log(response.data.visit_no);
      patient_surname_inpatient.innerHTML = `
            <label>Surname</label>
            <input class="form-control" name="patient_surname"  value=${response.data.surname} readonly/>`;

      patient_name_inpatient.innerHTML = `
            <label>First Name</label>
            <input class="form-control" name="patient_name"  value=${response.data.firstname} readonly/>`;
      PIN_IN_PATIENT.innerHTML = `
            <label>PIN no</label>
            <input type="text" class="form-control" name="patient_pin" value=${response.data.pin_no} readonly />
            `;

      if (response.data.admission_no) {
        console.log(response.data.admission_no);
        receipt_no_in_patient.innerHTML = `
                <div>
                <label>Admission No</label>
                <input type="text" class="form-control" name="admission_no" value=${response.data.admission_no} readonly />
                </div>
                
                `;
        patient_type_in_patient.innerHTML = `

                <label>Patient Type</label> 
                <input type="text" class="form-control" name="patient_type" value=${response.data.patient_type} readonly />
                `;
        phone_in_patient.innerHTML = `
                <label>phone no</label>
                <input type="text" class="form-control" name="phone" value=${response.data.phone} readonly id="phone" />
                `;
        gender_in_patient.innerHTML = `
                <label>Gender</label>
                <input type="text" class="form-control" name="gender" value=${response.data.gender} readonly id="gender" />
                `;
        date_of_birth_in_patient.innerHTML = `
                <label>Date of Birth</label>
                <input type="text" class="form-control" name="date_of_birth" value=${response.data.date_of_birth} readonly id="date_of_birth" />
                `;
        address_in_patient.innerHTML = `
                 <label>Address</label>
                <input type="text" class="form-control" name="address" value=${response.data.address} readonly id="address" />
                `;
        // admission_no.innerHTML = `
        //         <label>Admission no</label>
        //         <input type="text" class="form-control" name="admission_no" value=${response.data.admission_no} readonly />
        //         `;
      }
    },
  });
}

const sendSearchDataInpatient = async (patient) => {
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
        resultsBoxInpatient.innerHTML = "";
        response.data.forEach((patient) => {
          const pin_no = patient.pin_no.replace("P", "");

          resultsBoxInpatient.innerHTML += `<a href="/patient" class="item">
  
                        <div class="list-group">
                          
                        
                          
                            <a style="cursor:pointer;"   class="list-group-item list-group-item-action"  onClick="myFunction_inpatient(id=${pin_no})">${patient.pin_no}-${patient.surname}-${patient.name}</a>
                         
                        
  
                        
                    </div>
          
            </a>`;
        });
      } else {
        if (searchInput.value.length > 0) {
          resultsBoxInpatient.innerHTML = `<div class="list-group"><a href="#" class="list-group-item list-group-item-action">${response.data}</a></div>`;
        } else {
          resultsBoxInpatient.classList.add("d-none");
        }
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
};

searchInputInpatient.addEventListener("keyup", (e) => {
  if (e.target.value.length > 8) {
    console.log(e.target.value);
    if (resultsBoxInpatient.classList.contains("d-none")) {
      resultsBoxInpatient.classList.remove("d-none");
    }
    sendSearchDataInpatient(e.target.value);
  }
});
