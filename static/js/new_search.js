console.log("heelooo");

const url = window.location.href;
const searchForm = document.getElementById("KAL");
const searchInput = document.getElementById("search_input");
const patient_search = document.getElementById("patient_search");
const resultsBox1 = document.getElementById("results-box");
const crf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const form1 = document.getElementById("form-name");
const PIN = document.getElementById("pin_no");
const patient_id = document.getElementById("patient_id");
const patient_name = document.getElementById("patient_name");
const patient_surname = document.getElementById("patient_surname");
const visit_no = document.getElementById("visit_no");
const receipt_no = document.getElementById("receipt_no");
const patient_type = document.getElementById("patient_type");
const admission_no = document.getElementById("admission_no");

function myFunction(id) {
  resultsBox1.classList.add("d-none");

  console.log(id);
  $.ajax({
    type: "get",
    url: `get_patient/${id}`,
    success: (response) => {
      //   console.log(response.data.visit_no);
      console.log(response.data.receipt_no);
      console.log(response.data.invoice_no);

      patient_surname.innerHTML = `
            <label>Surname</label>
            <input class="form-control" name="patient_surname"  value=${response.data.surname} readonly/>`;

      patient_name.innerHTML = `
            <label>First Name</label>
            <input class="form-control" name="patient_name"  value=${response.data.firstname} readonly/>`;
      PIN.innerHTML = `
            <label>PIN no</label>
            <input type="text" class="form-control" name="patient_pin" value=${response.data.pin_no} readonly />
            `;
      visit_no.innerHTML = `
            <label>Visit no</label>
            <input type="text" class="form-control" name="visit_no" value=${response.data.visit_no} readonly />
            `;
      if (
        response.data.invoice_no
      ) {
        console.log(response.data.invoice_no);
        receipt_no.innerHTML = `
           
                <label>Invoice no</label>
                <input type="text" class="form-control" name="invoice_no" value=${response.data.invoice_no} readonly />
                `;
        patient_type.innerHTML = `
                <label>Patient Type</label>
                <input type="text" class="form-control" name="patient_type" value=${response.data.patient_type} readonly />
                `;
      } else if (
        response.data.receipt_no
      ) {
        receipt_no.innerHTML = `
                <label>Receipt no</label>
                <input type="text" class="form-control" name="receipt_no" value=${response.data.receipt_no} readonly />
                `;
        patient_type.innerHTML = `
                <label>Patient Type</label>
                <input type="text" class="form-control" name="patient_type" value=${response.data.patient_type} readonly />
                `;
      } else if ( response.data.extra_bill_no) {
        console.log(response.data.admission_no);
        receipt_no.innerHTML = `
                <label>Extra Bill no</label>
                <input type="text" class="form-control" name="receipt_no" value=${response.data.extra_bill_no} readonly />
                `;
        patient_type.innerHTML = `

                <label>Patient Type</label>
                <input type="text" class="form-control" name="patient_type" value=${response.data.patient_type} readonly />
                `;
                admission_no.innerHTML = `
                <label>Admission no</label>
                <input type="text" class="form-control" name="admission_no" value=${response.data.admission_no} readonly />
                `;
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
}

const sendSearchData = async (patient) => {
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
        resultsBox1.innerHTML = "";
        response.data.forEach((patient) => {
          const pin_no = patient.pin_no.replace("P", "");

          resultsBox1.innerHTML += `<a href="/patient" class="item">

                      <div class="list-group">
                        
                      
                        
                          <a style="cursor:pointer;"   class="list-group-item list-group-item-action"  onClick="myFunction(id=${pin_no})">${patient.pin_no}-${patient.surname}-${patient.name}</a>
                       
                      

                      
                  </div>
        
          </a>`;
        });
      } else {
        if (searchInput.value.length > 0) {
          resultsBox1.innerHTML = `<div class="list-group"><a href="#" class="list-group-item list-group-item-action">${response.data}</a></div>`;
        } else {
          resultsBox1.classList.add("d-none");
        }
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
};

searchInput.addEventListener("keyup", (e) => {
  if (e.target.value.length > 8) {
    console.log(e.target.value);
    if (resultsBox1.classList.contains("d-none")) {
      resultsBox1.classList.remove("d-none");
    }
    sendSearchData(e.target.value);
  }
});

console.log(crf);
console.log(url);
console.log(url);
