-- Curso--

CREATE TABLE curso(
id_curso INT PRIMARY KEY,
curso_nombre  VARCHAR(100)
);
-- Promoción--
CREATE TABLE promocion (
  id_promocion INT PRIMARY KEY,
  promocion VARCHAR(50),
  fecha DATE
);
--Sede

CREATE TABLE sede (
  id_sede INT PRIMARY KEY,
  nombre_sede VARCHAR(50)
);
-- Modalidad--
CREATE TABLE modalidad (
  id_modalidad INT PRIMARY KEY,
  nombre_modalidad VARCHAR(50)
);
-- Claustro--

CREATE TABLE claustro (

  id_claustro INT PRIMARY KEY,

  nombre VARCHAR(50),
  apellido VARCHAR(100),
  rol VARCHAR(50),
   id_curso INT,
   id_modalidad INT,
    id_promocion INT,
    id_sede INT,

  FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
  FOREIGN KEY (id_modalidad) REFERENCES modalidad(id_modalidad),
  FOREIGN KEY (id_promocion) REFERENCES promocion(id_promocion),  
  FOREIGN KEY (id_sede) REFERENCES sede(id_sede)




);

-- alumnos sin modalidad as FK

CREATE TABLE alumnos(
id_alumno INT PRIMARY KEY,
nombre VARCHAR(50),
apellido VARCHAR(100),
email VARCHAR(50),
id_promocion INT,
id_sede INT,
id_modalidad INT,
id_curso INT,

  FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
  FOREIGN KEY (id_promocion) REFERENCES promocion(id_promocion),  
	FOREIGN KEY (id_sede) REFERENCES sede(id_sede)
);


-- Notas FS

CREATE TABLE notas_FS(
expediente_FS INT PRIMARY KEY,
id_alumno INT,
Proyecto_WebDev VARCHAR(50),
Proyecto_FrontEnd VARCHAR(50),
Proyecto_Backend VARCHAR(50),
Proyecto_React VARCHAR(50),
Proyecto_FullSatck VARCHAR(50),
FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)

);

-- Notas DS

CREATE TABLE notas_DS(
expediente_DS INT PRIMARY KEY,
Proyecto_HLF VARCHAR(50),
Proyecto_EDA VARCHAR(50),
Proyecto_BBDD VARCHAR(50),
Proyecto_ML VARCHAR(50),
Proyecto_Deployment VARCHAR(50),
FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)
)





























