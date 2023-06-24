const url = window.location.href;

//?? out patient
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
const date_of_birth = document.getElementById("date_of_birth");
const phone = document.getElementById("phone");
const address = document.getElementById("address");
const gender = document.getElementById("gender");

const visit_no = document.getElementById("visit_no");
const receipt_no = document.getElementById("receipt_no");
const multiple_input = document.getElementById("multiple_input");

const patient_type = document.getElementById("patient_type");
const admission_no = document.getElementById("admission_no");
let totalQuantity = 0;
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
      if (response.data) {
        patient_surname.innerHTML = `
            <label>Surname</label>
            <input class="form-control" name="patient_surname"  value=${response.data.surname} readonly id="surname"/>`;

        patient_name.innerHTML = `
            <label>First Name</label>
            <input class="form-control" name="patient_name"  value=${response.data.firstname} readonly id="firstname"/>`;
        PIN.innerHTML = `
            <label>PIN no</label>
            <input type="text" class="form-control" name="patient_pin" value=${response.data.pin_no} readonly id="patient_pin" />
            `;
        phone.innerHTML = `
        <label>phone no</label>
        <input type="text" class="form-control" name="phone" value=${response.data.phone} readonly id="phone" />
        `;
        gender.innerHTML = `
        <label>Gender</label>
        <input type="text" class="form-control" name="gender" value=${response.data.gender} readonly id="gender" />
        `;
        date_of_birth.innerHTML = `
        <label>Date of Birth</label>
        <input type="text" class="form-control" name="date_of_birth" value=${response.data.date_of_birth} readonly id="date_of_birth" />
        `;
        address.innerHTML = `
         <label>Address</label>
        <input type="text" class="form-control" name="address" value=${response.data.address} readonly id="address" />
        `;
      } else if (response.error) {
        iziToast.warning({
          title: `${response.error}`,

          position: "topRight",
        });
      }

      if (response.data.invoice_no) {
        console.log(response.data.invoice_no);
        response.data.invoice_no.map((invoice, index) => {
          multiple_input.innerHTML += `
        <div style="margin-right:8px;">
            <label>Invocie no_${index + 1}</label>
            <input type="text" class="form-control" name="invocie_no" value=${
              invoice.invoiceno
            } readonly id="invocie_no_${index + 1}" />
          </div>
          `;
          multiple_input.innerHTML += `
          <div style="margin-right:8px;">
            <label>Visit no_${index + 1}</label>
            <input type="text" class="form-control" name="visit_no" value=${
              invoice.visitno_id
            } readonly id="visit_no_${index + 1}"/>
          </div>
          `;

          totalQuantity += invoice.quantity;
        });
        // receipt_no.innerHTML = `

        //         <label>Invoice no</label>
        //         <input type="text" class="form-control" name="invoice_no" value=${response.data.invoice_no} readonly />
        //
        multiple_input.innerHTML += `
        <div style="margin-right:8px;">
        <label>Quantity of Sessions Paid for</label>
        <input type="text" class="form-control" name="totalquantity" value=${totalQuantity} readonly />
        </div>        `;
        patient_type.innerHTML = `
                <label>Patient Type</label>
                <input type="text" class="form-control" name="patient_type" value=${response.data.patient_type} readonly />
                `;
      } else if (response.data.receipt_no) {
        response.data.receipt_no.map((receipt, index) => {
          console.log(receipt);
          multiple_input.innerHTML += `
          <div style="margin-right:8px;">
            <label>Receipt no_${index + 1}</label>
            <input type="text" class="form-control" name="receipt_no" value=${
              receipt.receiptno_id
            } readonly id="receipt_no_${index + 1}"/>
          </div>
          `;
          multiple_input.innerHTML += `
          <div style="margin-right:8px; width:60px;">
          <label> Quantity_${index + 1}</label>
          <input type="text" class="form-control" name="quantity" value=${
            receipt.quantity
          } readonly id="receipt_no_${index + 1}"/>
        </div>
        `;
          multiple_input.innerHTML += `
          <div style="margin-right:8px;">
            <label>Visit no_${index + 1}</label>
            <input type="text" class="form-control" name="visit_no" value=${
              receipt.visitno_id
            } readonly  id="Visit no_${index + 1}"/>
          </div>
          `;

          totalQuantity += receipt.quantity;
        });

        multiple_input.innerHTML += `
        <div style="margin-right:8px;">
        <label>Quantity of Sessions Paid for</label>
        <input type="text" class="form-control" name="totalquantity" value=${totalQuantity} readonly id="quantity"/>
        </div>

          `;
        patient_type.innerHTML = `
                <label>Patient Type</label>
                <input type="text" class="form-control" name="patient_type" value=${response.data.patient_type} readonly  id="patient_type"/>
                `;
      }
    },
    error: (error) => {
      console.log(error);
      if (error.responseJSON.patient_doesnot_exist) {
        iziToast.warning({
          title: `${error.responseJSON.patient_doesnot_exist}`,

          position: "topRight",
        });
        setTimeout(() => {
          window.location.href = `${window.location.origin}/patient_profile/${error.responseJSON.patient_no}`;
        }, 4000);
      } else {
        iziToast.warning({
          title: `${error.responseJSON.message}`,

          position: "topRight",
        });
      }
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
