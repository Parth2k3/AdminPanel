function edit(id, name, salary, position) {
  // Replace the div with input fields to edit the employee data
  var employeeDiv = document.getElementById(id);
  employeeDiv.innerHTML = `
    <input type="text" id="name_${id}" value="${name}">
    <input type="number" id="salary_${id}" value="${salary}">
    <input type="text" id="position_${id}" value="${position}">
    <button class="btn btn-primary update-btn" onclick='update(${id})'">Update</button>
  `;
}

function update(id){
  var name = document.getElementById(`name_${id}`).value;
  var position = document.getElementById(`position_${id}`).value;
  var salary = document.getElementById(`salary_${id}`).value;
  var data = {
      id: id,
      name: name,
      position: position,
      salary: salary
  };
  
  fetch('/update',{
    method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
        })
  .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            location.reload();

            return response.json();
  })
}

function add_employee(){
  var name = document.getElementById('floatingName').value;
  var position = document.getElementById('floatingPosition').value;
  var salary = document.getElementById('floatingSalary').value;
  var data = {
        name: name,
        position: position,
        salary: salary
    };

    fetch('/add',{
      method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
          })
    .then(response => {
              if (!response.ok) {
                  throw new Error('Network response was not ok');
              }
              location.reload();

              return response.json();
    })
  }

function search_by_name(){
  var name = document.getElementById('search-by-name').value;
  window.location.href = `/employees/name/${name}`;
  return 
}

function search_by_pos(){
  var pos = encodeURIComponent(document.getElementById('search-by-pos').value);
  var url = `/employees/position/${pos}`;
  window.location.href = url;
  return
}


function search_by_salary(){
  var min = document.getElementById('search-by-min').value;
  var max = document.getElementById('search-by-max').value;
  var min = parseInt(min);
  var max = parseInt(max);
  if (!min && min !== 0) {
      min = -1;
  }
  if (!max && max !== 0) {
      max = Number.MAX_SAFE_INTEGER;
  }
  console.log(min, max)
  window.location.href = `/employees/salarybw/${min}/${max}`;
  return
}