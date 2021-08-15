CREATE TABLE "proyectoDesarrollo" (
  "id" SERIAL PRIMARY KEY,
  "descripcion" varchar(255),
  "empresaAsociada" int
);

CREATE TABLE "historiaUsuario" (
  "id" SERIAL PRIMARY KEY,
  "idProyectoDesarrollo" int,
  "descripcion" varchar(255)
);

CREATE TABLE "ticketDesarrollo" (
  "id" int,
  "idHistoriUsuario" int,
  "usuario" int,
  "descripcion" varchar(255),
  "estatus" boolean
);

CREATE TABLE "usuarios" (
  "id" SERIAL PRIMARY KEY,
  "usuario" varchar(255),
  "contraseña" varchar(255),
  "asociacionEmpresa" int
);

CREATE TABLE "empresa" (
  "id" SERIAL PRIMARY KEY,
  "nombre" varchar(255),
  "nit" varchar(255),
  "telefono" varchar(255),
  "direccion" varchar(255),
  "correo" varchar(255)
);
