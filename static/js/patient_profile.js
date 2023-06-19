// function
function get_patient_admission_id(patient_id) {
  const patient_admission_no = document.getElementById("patient_admission_no");
  $.ajax({
    type: "GET",
    url: `/get_patient_admission_no/${patient_id}`,
    success: function (data) {
      const physio_admission_no = data.physio_admission_no;
      patient_admission_no.value = physio_admission_no;
      // patient_admission_id.innerHTML = data;
    },
  });
}
