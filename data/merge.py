from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
CSV_FILE = ROOT / "Proyecto" / "data"
NUEVOS= CSV_FILE / "nuevas"

df1 = pd.read_csv(CSV_FILE / "clase_1.csv", sep=";")
df2 = pd.read_csv(CSV_FILE / "clase_2.csv", sep=";")
df3 = pd.read_csv(CSV_FILE / "clase_3.csv", sep=";")
df4 = pd.read_csv(CSV_FILE / "clase_4.csv", sep=";")
df5 = pd.read_csv(CSV_FILE / "claustro.csv", sep=";")
df_6 = pd.read_csv(CSV_FILE / "df_total.csv", sep=",")
df_6 = df_6.rename(columns={df_6.columns[2]: "Promocion"})


curso = pd.DataFrame({
    "id_curso": [0, 1],
    "curso_nombre": ["Data Science", "Full Stack"],})

curso.to_csv(NUEVOS / "curso.csv",index = False)

promocion = df_6[
    ["Promocion", "Fecha_comienzo"]].drop_duplicates().reset_index(drop=True)

promocion = promocion.rename(
    columns={
        "Promocion": "promocion",
        "Fecha_comienzo": "fecha_comienzo"})
promocion["fecha_comienzo"] = pd.to_datetime(
    promocion["fecha_comienzo"],
    format="%d/%m/%Y")
promocion["id_promocion"] = range(len(promocion))
promocion = promocion[["id_promocion", "promocion", "fecha_comienzo"]]
print(promocion)
promocion.to_csv(NUEVOS / "promocion.csv",index = False)

curso = pd.DataFrame({"id_curso": [0, 1],"curso_nombre": ["DS", "FS"],})
print(curso)
curso.to_csv(NUEVOS / "curso.csv",index = False)

sede = pd.DataFrame({"id_sede": [0, 1],"nombre_sede": ["Madrid", "Valencia"],})
print(curso)
sede.to_csv(NUEVOS / "sede.csv",index = False)

modalidad = pd.DataFrame({"id_curso": [0, 1],"nombre_modalidad": ["Online", "Presencial"],})
print(modalidad)
modalidad.to_csv(NUEVOS / "modalidad.csv",index = False)


nombre_claustro = df5["Nombre"].str.rsplit(" ",n=1,expand=True)

claustro = pd.DataFrame({"id_claustro": range(1, len(df5) + 1),"nombre": nombre_claustro[0],
    "apellido": nombre_claustro[1],"rol": df5["Rol"],"id_curso": df5["Vertical"].map({
        "DS": 0,
        "FS": 1}),

    "id_modalidad": df5["Modalidad"].map({"Online": 0,"Presencial": 1}),

    "id_promocion": df5["Promocion"].map({"Septiembre": 0,"Febrero": 1}),

    "id_sede": df5["Campus"].map({"Madrid": 0,"Valencia": 1})})

columnas_id = ["id_claustro","id_curso","id_modalidad","id_promocion","id_sede"]

claustro[columnas_id] = claustro[columnas_id].astype(int)

claustro.to_csv(NUEVOS / "tabla_claustro.csv",index=False)
print(claustro)

nombre_alumnos = df_6["Nombre"].str.rsplit(" ",n=1,expand=True)
df_6 = df_6.rename(columns={"PromociÃ³n": "Promocion"})
alumnos = pd.DataFrame({
    "id_alumno": range(1, len(df_6) + 1),
    "nombre": nombre_alumnos[0],
    "apellido": nombre_alumnos[1],
    "email": df_6["Email"],       
    "id_promocion": df_6["Promocion"].str.strip().map({
        "Septiembre": 0,
        "Febrero": 1}),
    "id_sede": df_6["Campus"].map({
        "Madrid": 0,
        "Valencia": 1}),
    "id_modalidad": 1,
    "id_curso": df_6["curso"].map({
            "Data": 0,
            "Full": 1}),

    })

print(alumnos)
print(df_6.shape)
print(df_6.columns)
print(alumnos)
alumnos.to_csv(NUEVOS / "alumnos.csv",index = False)

df_6["id_alumno"] = range(1, len(df_6) + 1)

notas_FS = df_6[df_6["curso"] == "Full"].copy()
notas_FS["expediente_FS"] = range(1,len(notas_FS) + 1)
notas_FS = notas_FS[["expediente_FS","id_alumno","Proyecto_WebDev","Proyecto_FrontEnd",
    "Proyecto_Backend","Proyecto_React","Proyecto_FullSatck"]]
notas_FS.to_csv(NUEVOS / "notas_FS.csv",index=False)
print(notas_FS)

df_6["id_alumno"] = range(1, len(df_6) + 1)
notas_DS = df_6[df_6["curso"] == "Data"].copy()
notas_DS["expediente_FS"] = range(1,len(notas_DS) + 1)
notas_DS = notas_DS[[ "expediente_FS","id_alumno","Proyecto_HLF","Proyecto_EDA",
    "Proyecto_BBDD","Proyecto_ML","Proyecto_Deployment"]]
notas_DS.to_csv(NUEVOS / "notas_DS.csv",index=False)

print(notas_DS)

