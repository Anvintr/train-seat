
$(document).ready(function () {
  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });
  $('#dismiss, .overlay').on('click', function () {
    $('#sidebar').removeClass('active');
  });
});




document.addEventListener('DOMContentLoaded', () => {
  const ctx = document.getElementById("userChart").getContext("2d");

  // Data
  const labels = ["January", "February", "March", "April", "May", "June"];
  const users = [1500, 800, 3000, 500, 9000, 4500];
  const bookings = [5600, 3300, 4000, 2900, 6000, 5690];

  const data = {
    labels: labels,
    datasets: [
      {
        label: "Users",
        data: users,
        backgroundColor: "rgba(54, 162, 235, 0.7)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
      },
      {
        label: "Bookings",
        data: bookings,
        backgroundColor: "rgba(255, 99, 132, 0.7)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
      },
    ],
  };

  const config = {
    type: "bar",
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
          labels: {
            color: "#000", // Legend text color
          },
        },
        title: {
          display: true,
          text: "Monthly Users & Bookings Analysis",
          font: {
            size: 18,
          },
          color: "#333",
        },
      },
      scales: {
        x: {
          stacked: false,
          title: {
            display: true,
            text: "Months",
            color: "#333",
          },
          ticks: {
            color: "#000",
          },
        },
        y: {
          stacked: false,
          beginAtZero: true,
          title: {
            display: true,
            text: "Count",
            color: "#333",
          },
          ticks: {
            color: "#000",
          },
        },
      },
    },
  };

  new Chart(ctx, config);
});


// Pie Diagram: Bookings by Routes
const pieCtx = document.getElementById('pieChart').getContext('2d');
const pieChart = new Chart(pieCtx, {
  type: 'pie',
  data: {
    labels: ['Route A', 'Route B', 'Route C', 'Route D'],
    datasets: [{
      data: [3000, 1500, 1000, 2200],
      backgroundColor: [
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)'
      ],
      borderColor: '#fff',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
  }
});

// Open Modal
function openModel() {
  const routeModal = new bootstrap.Modal(document.getElementById('AddModal'));
  routeModal.show();
}
// Open the modal for editing
function openEditModal(button) {

  const source = button.getAttribute("data-source");
  const destination = button.getAttribute("data-destination");
  // Set the values in the modal
  document.getElementById("source").value = source;
  document.getElementById("destination").value = destination;

    

  const name = button.getAttribute("data-name");
  document.getElementById("name").value = name;
   // Set the selected option in the route dropdown
   const selectElement = document.getElementById('route');
   selectElement.value = routeId; 




  // Show the modal
  const modal = new bootstrap.Modal(document.getElementById("Modal"));
  modal.show();
}

function openEditStationModal(button) {
  // Get the route ID and name from the data attributes of the button
  const routeId = button.getAttribute('data-route-id');
  const name = button.getAttribute('data-name');

  // Set the selected option in the route dropdown based on routeId
  const selectElement = document.getElementById('route');
  selectElement.value = routeId; // This sets the default selected option based on the routeId

  // Set the name in the input field
  const nameInput = document.getElementById('name');
  nameInput.value = name; // Set the name as the value of the input field

  // Show the modal (Bootstrap 5 method)
  const modal = new bootstrap.Modal(document.getElementById('EditModal'));
  modal.show();
}

function openEditTrainModal(button) {
  // Get the route ID and name from the data attributes of the button
  const routeId = button.getAttribute('data-route-id');
  const name = button.getAttribute('data-name');
  const number = button.getAttribute('data-train-number');

  // Set the selected option in the route dropdown based on routeId
  const selectElement = document.getElementById('route');
  selectElement.value = routeId; // This sets the default selected option based on the routeId

  const numberInput = document.getElementById('number');
  numberInput.value = number; 
  // Set the name in the input field
  const nameInput = document.getElementById('name');
  nameInput.value = name; // Set the name as the value of the input field


  // Show the modal (Bootstrap 5 method)
  const modal = new bootstrap.Modal(document.getElementById('EditModal'));
  modal.show();
}

  // Toggle the visibility of time inputs
  function toggleTime(checkbox) {
    const timeDiv = checkbox.closest('.status').querySelector('.create-time');
    const arrivalInput = timeDiv.querySelector('.arrival-time');
    const departureInput = timeDiv.querySelector('.departure-time');

    if (checkbox.checked) {
      timeDiv.style.display = 'block';
      arrivalInput.setAttribute('required', 'required');
      departureInput.setAttribute('required', 'required');
    } else {
      timeDiv.style.display = 'none';
      arrivalInput.removeAttribute('required');
      departureInput.removeAttribute('required');
    }
  }

  function openEditCompartmentModal(button) {
    // Get the route ID and name from the data attributes of the button
    const name = button.getAttribute('data-name');
    const number = button.getAttribute('data-train-number');
    const compartment = button.getAttribute('data-compartment');
    const capacity = button.getAttribute('data-capacity');

  
  
    // Set the name in the input field
    const nameInput = document.getElementById('name');
    nameInput.value = `${number}-${name}`; 
      
    const compartmentInput = document.getElementById('compartment');
    compartmentInput.value = compartment; // Set the name as the value of the input field
  
    const capacityInput = document.getElementById('capacity');
    capacityInput.value = capacity;
    // Show the modal (Bootstrap 5 method)
    const modal = new bootstrap.Modal(document.getElementById('EditModal'));
    modal.show();
  }








// JavaScript to set the complaint ID in the modal title when a "Reply" button is clicked
document.querySelectorAll('.reply-btn').forEach(button => {
  button.addEventListener('click', function () {
    const complaintId = this.getAttribute('data-complaint-id');
    document.querySelector('.modal-title-id').textContent = complaintId;
  });
});

// JavaScript to handle form submission
document.getElementById('replyForm').addEventListener('submit', function (event) {
  // Prevent the default form submission
  event.preventDefault();


  // Display success message
  alert('Reply sent successfully!');

  // Close the modal
  $('#replyModal').modal('hide');
});