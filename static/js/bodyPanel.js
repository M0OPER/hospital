document.write(`
<ul class="nav nav-tabs justify-content-center" id="myTab" role="tablist">
  <li class="nav-item">
   <a class="nav-link active" id="citas-tab" data-toggle="tab" href="#citas" role="tab" aria-controls="citas" aria-selected="true">CITAS</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="medicos-tab" data-toggle="tab" href="#medicos" role="tab" aria-controls="medicos" aria-selected="false">MEDICOS</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="pacientes-tab" data-toggle="tab" href="#pacientes" role="tab" aria-controls="pacientes" aria-selected="false">PACIENTES</a>
  </li>
</ul>
<div class="tab-content" id="myTabContent">
  <div class="tab-pane fade show active" id="citas" role="tabpanel" aria-labelledby="citas-tab">
    <div class="modal-body">
      <div class="form-group">
        <div class="row">
          <div class="col-4">
            <input id="pnlBuscar" name="pnlBuscar" type="text" class="form-control" placeholder="BUSCAR CITAS...">
          </div>
          <div class="col-2">
            <select class="form-control text-white bg-dark manita" id="exampleFormControlSelect1">
           <option>Medicos</option>
           <option>Fecha</option>
           <option>Hora</option>
          </select>
          </div>
          <div class="col-2 ">
            <i class="bi bi-search close manita float-left" aria-label="Close"></i>
          </div>
        </div>
        <hr>
        <h6>LISTADO CITAS</h6>
        <hr>
        <div>
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">MEDICO</th>
                <th scope="col">FECHA</th>
                <th scope="col">HORA</th>
                <th scope="col">DETALLES</th>
                <th scope="col">EDITAR</th>
                <th scope="col">CANCELAR</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>JUANCHO POLO GRACIAS</td>
                <td>12/12/2020</td>
                <td>12:00 PM</td>
                <td><i class="bi bi-eye-fill close manita float-left detalles"data-toggle="modal" data-target="#modalDetallesCita" aria-label="Close"></i></td>
                <td><i class="bi bi-pencil-fill close manita float-left editar" aria-label="Close"></i></td>
                <td><i class="bi bi-x-square-fill close manita float-left cancelar" data-toggle="modal" data-target="#modalCancelarCita" aria-label="Close"></i></td>
              </tr>
            </tbody>
          </table>
        </div>
        <button id="pnlSolicitar" type="button" class="btn btn-verde btn-lg">SOLICITAR CITA</button>
      </div>
    </div>
  </div>
  <div class="tab-pane fade" id="medicos" role="tabpanel" aria-labelledby="medicos-tab">
    <div class="modal-body">
      <div class="form-group">
        <div class="row">
          <div class="col-4">
            <input id="pnlBuscar" name="pnlBuscar" type="text" class="form-control" placeholder="BUSCAR MEDICOS...">
          </div>
          <div class="col-2 ">
            <i class="bi bi-search close manita float-left" aria-label="Close"></i>
          </div>
        </div>
        <hr>
        <h6>LISTADO MEDICOS</h6>
        <hr>
        <div>
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">NOMBRES</th>
                <th scope="col">CEDULA</th>
                <th scope="col">CITAS ASIGNADAS</th>
                <th scope="col">DETALLES</th>
                <th scope="col">EDITAR</th>
                <th scope="col">BLOQUEAR</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>JUANCHO POLO GRACIAS</td>
                <td>12/12/2020</td>
                <td>12:00 PM</td>
                <td><i class="bi bi-eye-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-pencil-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-x-square-fill close manita float-left" aria-label="Close"></i></td>
              </tr>
            </tbody>
          </table>
        </div>
        <button id="pnlSolicitar" type="button" class="btn btn-verde btn-lg">SOLICITAR CITA</button>
      </div>
    </div>
  </div>
  <div class="tab-pane fade" id="pacientes" role="tabpanel" aria-labelledby="pacientes-tab">
    <div class="modal-body">
      <div class="form-group">
        <div class="row">
          <div class="col-4">
            <input id="pnlBuscar" name="pnlBuscar" type="text" class="form-control" placeholder="BUSCAR PACIENTES...">
          </div>
          <div class="col-2 ">
            <i class="bi bi-search close manita float-left" aria-label="Close"></i>
          </div>
        </div>
        <hr>
        <h6>LISTADO PACIENTES</h6>
        <hr>
        <div>
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">NOMBRES</th>
                <th scope="col">CEDULA</th>
                <th scope="col">CITAS ASIGNADAS</th>
                <th scope="col">DETALLES</th>
                <th scope="col">EDITAR</th>
                <th scope="col">BLOQUEAR</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>JUANCHO POLO GRACIAS</td>
                <td>12/12/2020</td>
                <td>12:00 PM</td>
                <td><i class="bi bi-eye-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-pencil-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-x-square-fill close manita float-left" aria-label="Close"></i></td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
                <td><i class="bi bi-eye-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-pencil-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-x-square-fill close manita float-left" aria-label="Close"></i></td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
                <td><i class="bi bi-eye-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-pencil-fill close manita float-left" aria-label="Close"></i></td>
                <td><i class="bi bi-x-square-fill close manita float-left" aria-label="Close"></i></td>
              </tr>
            </tbody>
          </table>
        </div>
        <button id="pnlSolicitar" type="button" class="btn btn-verde btn-lg">SOLICITAR CITA</button>
      </div>
    </div>
  </div>
</div>

`);