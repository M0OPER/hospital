from sqlite3 import Error
import sqlite3, sys
def sql_connection():
    try:
        msg =  sqlite3.connect('hospital.db')
        return msg
    except Error as e:
        return "Error al contactar en la base de datos"

def qry_soporte(cod):
  try:
    qry = "select * FROM soporte WHERE sop_cod = '" + cod + "'"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchall()
    return result
  except Error as e:
    return "Error al cargar datos"
  
def qry_iniciar_sesion(email):
  try:
    qry = "SELECT usu_id, usu_hash_pass, pac_nombres || ' ' || pac_apellidos, sop_datos, usu_estado FROM usuarios, soporte INNER JOIN pacientes on usu_id = pac_usuario_id WHERE usu_email = '" + email + "' AND usu_tipo_usu = sop_id UNION SELECT usu_id, usu_hash_pass, med_nombres || ' ' || med_apellidos, sop_datos, usu_estado FROM usuarios, soporte INNER JOIN medicos on usu_id = med_usuario_id WHERE usu_email = '" + email + "' AND usu_tipo_usu = sop_id UNION SELECT usu_id, usu_hash_pass, adm_nombres || ' ' || adm_apellidos, sop_datos, usu_estado FROM usuarios, soporte INNER JOIN administradores on usu_id = adm_usuario_id WHERE usu_email = '" + email + "' AND usu_tipo_usu = sop_id"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al guardar datos"

def qry_verificar_password(id):
  try:
    qry = "SELECT usu_hash_pass FROM usuarios WHERE usu_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al guardar datos"

def qry_cambiar_password(id, hash):
  try:
    qry = "UPDATE usuarios SET usu_hash_pass = '" + hash + "' WHERE usu_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Datos guardados con exito"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_cambiar_password_reco(email, hash):
  try:
    qry = "UPDATE usuarios SET usu_hash_pass = '" + hash + "', usu_token_reco = '' WHERE usu_email = '" + email + "'"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Datos guardados con exito"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_restablecer_password(email, token):
  try:
    qry = "UPDATE usuarios SET usu_token_reco = '" + token + "' WHERE usu_email = '" + email + "'"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "OK"
  except sqlite3.Error as error:
    print(error, file=sys.stderr)
    return "ERROR"

def qry_cargar_usuario(id, rol, usuario):
  try:
    qry = "SELECT " + rol + "_nombres, " + rol + "_apellidos, sop_datos, " + rol + "_identificacion, " + rol + "_telefono, " + rol + "_direccion, " + rol + "_fecha_nacimiento, " + rol + "_edad, " + rol + "_sexo, usu_email FROM usuarios, soporte INNER JOIN " + usuario + " on usu_id = " + rol + "_usuario_id WHERE " + rol + "_id = " + id + " AND " + rol + "_tipo_identificacion = sop_id "
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    print(qry, file=sys.stderr)
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_detalles_usuario(id, rol, usuario):
  try:
    qry = "SELECT " + rol + "_nombres, " + rol + "_apellidos, sop_datos, " + rol + "_identificacion, " + rol + "_telefono, " + rol + "_direccion, " + rol + "_fecha_nacimiento, " + rol + "_edad, " + rol + "_sexo, usu_email FROM usuarios, soporte INNER JOIN " + usuario + " on usu_id = " + rol + "_usuario_id WHERE " + rol + "_usuario_id = " + id + " AND " + rol + "_tipo_identificacion = sop_id "
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    print(qry, file=sys.stderr)
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_actualizar_usuario(id, rol, usuario, nombres, apellidos, telefono, direccion, fecha_nacimiento, edad, sexo):
  try:
    qry = "UPDATE " + usuario + " SET " + rol + "_nombres = '" + nombres + "', " + rol + "_apellidos = '" + apellidos + "', " + rol + "_telefono = " + telefono + ", " + rol + "_direccion = '" + direccion + "', " + rol + "_fecha_nacimiento = '" + fecha_nacimiento + "', " + rol + "_edad = " + edad + ", " + rol + "_sexo = " + sexo + " WHERE " + rol + "_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Datos guardados con exito"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_bloquear_usuario(id):
  try:
    qry = "UPDATE usuarios SET usu_estado = 9 WHERE usu_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Datos guardados con exito"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_desbloquear_usuario(id):
  try:
    qry = "UPDATE usuarios SET usu_estado = 10 WHERE usu_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Datos guardados con exito"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_session_id(id, rol, usuario):
  try:
    qry = "SELECT " + usuario + "_id FROM usuarios, " + rol + " WHERE usu_id = '" + id + "' AND usu_id = " + usuario + "_usuario_id"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    return result
  except Error as e:
    return "Error al cargar datos"

def qry_registrar_usuario(email, token, hash, fecha, rol, estado):
  try:
    qry = "INSERT INTO usuarios (usu_email, usu_token, usu_hash_pass, usu_created_at, usu_tipo_usu, usu_estado) VALUES ('" + email + "', '" + token + "', '" + hash + "', '" + fecha + "', " + rol + ", " + estado + ");"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    last_id = cursorObj.lastrowid
    con.commit()
    con.close()
    return last_id
  except Error as e:
    print(e, file=sys.stderr)

def qry_registrar_medico(email, token, hash, fecha, rol, estado):
  try:
    qry = "INSERT INTO usuarios (usu_email, usu_token, usu_hash_pass, usu_created_at, usu_tipo_usu, usu_estado) VALUES ('" + email + "', '" + token + "', '" + hash + "', '" + fecha + "', " + rol + ", " + estado + ");"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    last_id = cursorObj.lastrowid
    con.commit()
    con.close()
    return last_id
  except Error as e:
    print(e, file=sys.stderr)

def qry_registrar_userId(id, rol, usuario, num_doc, tipo_doc, nombres, apellidos, telefono, direccion):
  try:
    qry = "INSERT INTO " + rol + " (" + usuario + "_usuario_id, pac_identificacion, pac_tipo_identificacion, pac_nombres, pac_apellidos, pac_telefono, pac_direccion) VALUES (" + id + ", " + num_doc + ", " + tipo_doc + ", '" + nombres + "', '" + apellidos + "', " + telefono + ", '" + direccion + "');"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Guardada con exito"
  except Error as e:
    print("error", file=sys.stderr)

def qry_registrar_userIdMedico(id, rol, usuario, num_doc, tipo_doc, nombres, apellidos, telefono, direccion, limite, especialidad):
  try:
    qry = "INSERT INTO " + rol + " (" + usuario + "_usuario_id, med_identificacion, med_tipo_identificacion, med_nombres, med_apellidos, med_telefono, med_direccion, med_limite_citas, med_especialidad_id) VALUES (" + id + ", " + num_doc + ", " + tipo_doc + ", '" + nombres + "', '" + apellidos + "', " + telefono + ", '" + direccion + "', " + limite + ", " + especialidad + ");"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Guardada con exito"
  except Error as e:
    print("error", file=sys.stderr)

def qry_verificar_token(email, token):
  try:
    qry = "SELECT usu_email, usu_token FROM usuarios WHERE usu_email = '" + email + "' AND usu_token = '" + token + "'"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    return result
  except Error as e:
    return "Error al guardar datos"

def qry_verificar_token_password(email, token):
  try:
    qry = "SELECT usu_email, usu_token FROM usuarios WHERE usu_email = '" + email + "' AND usu_token_reco = '" + token + "'"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    return result
  except Error as e:
    return "Error al guardar datos"

def qry_activar_cuenta(email, token):
  try:
    qry = "UPDATE usuarios SET usu_estado = 10, usu_token = '' WHERE usu_email = '" + email + "' AND usu_token = '" + token + "'"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "Tu cuenta ha sido activada"
  except Error as e:
    return "Error al guardar datos"

def qry_listar_citas_paciente(id, texto):
  try:
    qry = "SELECT cit_id, sop_datos, med_nombres  || ' ' || med_apellidos, cit_fecha_hora FROM citas, medicos, soporte WHERE cit_paciente_id = '" + id + "' AND cit_medico_id = med_id AND cit_estado = sop_id " + texto + " ORDER BY cit_created_at DESC"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchall()
    print(result, file=sys.stderr)
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_listar_citas_medico(id, texto):
  try:
    qry = "SELECT cit_id, sop_datos, pac_nombres  || ' ' || pac_apellidos, cit_fecha_hora FROM citas, pacientes, soporte WHERE cit_medico_id = '" + id + "' AND cit_paciente_id = pac_id AND cit_estado = sop_id " + texto + " ORDER BY cit_created_at DESC"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchall()
    print(result, file=sys.stderr)
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_listar_citas_administrador(texto):
  try:
    qry = "SELECT cit_id, sop_datos, med_nombres  || ' ' || med_apellidos, pac_nombres  || ' ' || pac_apellidos, cit_fecha_hora FROM citas, pacientes, soporte, medicos WHERE cit_medico_id = med_id AND cit_paciente_id = pac_id AND cit_estado = sop_id " + texto + " ORDER BY cit_created_at DESC"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchall()
    print(result, file=sys.stderr)
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_listar_medicos_administrador(texto):
  try:
    qry = "SELECT med_usuario_id, med_nombres, med_apellidos, med_identificacion, usu_estado FROM medicos, usuarios WHERE usu_id = med_usuario_id " + texto + " ORDER BY med_nombres ASC"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchall()
    print(result, file=sys.stderr)
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos "

def qry_listar_pacientes_administrador(texto):
  try:
    qry = "SELECT pac_usuario_id, pac_nombres, pac_apellidos, pac_identificacion, usu_estado FROM pacientes, usuarios WHERE usu_id = pac_usuario_id " + texto + " ORDER BY pac_nombres ASC"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchall()
    print(result, file=sys.stderr)
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

#DETALLES CITAS
def qry_cargar_especialidades_solicitar_cita():
  try:
    qry = "SELECT sop_id, sop_datos FROM soporte WHERE sop_cod = 'ESPE'"
    con = sql_connection()
    cur = con.cursor()
    cur.execute(qry)
    result = cur.fetchall()
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_cargar_medicos_solicitar_cita(especialidad):
  try:
    qry = "SELECT med_id, med_nombres || ' ' || med_apellidos as nombres, med_limite_citas FROM medicos, usuarios WHERE med_usuario_id = usu_id AND usu_estado = 10 AND med_especialidad_id =" + especialidad
    con = sql_connection()
    cur = con.cursor()
    cur.execute(qry)
    result = cur.fetchall()
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_verificar_medicos_solicitar_cita(id):
  try:
    qry = "SELECT COUNT(cit_medico_id) FROM citas WHERE cit_medico_id = " + id
    con = sql_connection()
    cur = con.cursor()
    cur.execute(qry)
    result = cur.fetchone()
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_detalles_cita_paciente(id):
  try:
    qry = "SELECT sop_datos, med_nombres, med_apellidos, pac_nombres, pac_apellidos, cit_fecha_hora, cit_detalle, IFNULL(his_texto, ''), IFNULL(com_texto_paciente, ''), IFNULL(com_texto_medico, '') FROM citas, medicos, soporte, pacientes LEFT JOIN historia ON cit_id = his_cita_id LEFT JOIN comentarios ON cit_id = com_cita_id WHERE cit_id = " + id + " AND cit_medico_id = med_id AND cit_estado = sop_id AND cit_paciente_id = pac_id"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    return result
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_solicitar_cita(paciente, medico, fechaHora, fecha, detalle):
  try:
    qry = "INSERT INTO citas (cit_paciente_id, cit_medico_id, cit_fecha_hora, cit_created_at, cit_detalle, cit_estado) VALUES (" + paciente + ", " + medico + ", '" + fechaHora + "', '" + fecha + "', '" + detalle + "', 13)"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    last_id = cursorObj.lastrowid
    con.commit()
    con.close()
    return "OK"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_atender_cita(cita, historia):
  try:
    qry = "INSERT INTO historia (his_texto, his_cita_id) VALUES ('" + historia + "', " + cita + ")"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    print("###", file=sys.stderr)
    return "OK"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_actualizar_estado_cita(cita):
  try:
    qry = "UPDATE citas SET cit_estado = 16 WHERE cit_id = " + cita
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "OK"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cargar datos"

def qry_cancelar_cita(id):
  try:
    qry = "UPDATE citas SET cit_estado = 14 WHERE cit_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "OK"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al cancelar cita"

def qry_aceptar_cita(id):
  try:
    qry = "UPDATE citas SET cit_estado = 15 WHERE cit_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "OK"
  except Error as e:
    print(e, file=sys.stderr)
    return "Error al aceptar cita"

def qry_insertar_comentarios(id):
  try:
    qry = "INSERT INTO comentarios (com_texto_paciente, com_texto_medico, com_cita_id) VALUES ('', '', " + id + ")"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "OK"
  except Error as e:
    return "Error al cargar datos"

def qry_actualizar_comentarios(id, paciente, medico):
  try:
    qry = "UPDATE comentarios SET com_texto_paciente = '" + paciente + "', com_texto_medico = '" + medico + "' WHERE com_cita_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    con.commit()
    con.close()
    return "OK"
  except Error as e:
    return "Error al cargar datos"

def qry_cargar_comentarios(id):
  try:
    qry = "SELECT * FROM comentarios WHERE com_cita_id = " + id
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(qry)
    result = cursorObj.fetchone()
    return result
  except Error as e:
    return "Error al cargar datos"