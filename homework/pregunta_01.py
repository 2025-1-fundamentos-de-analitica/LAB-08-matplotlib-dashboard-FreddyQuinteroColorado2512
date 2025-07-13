# pylint: disable=line-too-long
"""
Escriba el código que ejecute la acción solicitada.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envíos
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`
    * `Mode_of_Shipment`
    * `Customer_rating`
    * `Weight_in_gms`

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.
    * Todos los archivos deben ser creados en la carpeta `docs`.
    * Su código debe crear la carpeta `docs` si no existe.
    """

    # Crear carpeta docs si no existe
    os.makedirs("docs", exist_ok=True)

    # Leer el archivo CSV
    df = pd.read_csv("files/input/shipping-data.csv")

    # Gráfico 1: Distribución por bloque de almacén
    plt.figure()
    df['Warehouse_block'].value_counts().plot(kind='bar')
    plt.title("Shipping per Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # Gráfico 2: Modo de envío
    plt.figure()
    df['Mode_of_Shipment'].value_counts().plot(kind='bar')
    plt.title("Mode of Shipment")
    plt.xlabel("Mode")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # Gráfico 3: Calificación del cliente
    plt.figure()
    df['Customer_rating'].value_counts().sort_index().plot(kind='bar')
    plt.title("Customer Rating")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    # Gráfico 4: Distribución del peso
    plt.figure()
    df['Weight_in_gms'].plot(kind='hist', bins=20)
    plt.title("Weight Distribution")
    plt.xlabel("Weight (g)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()
