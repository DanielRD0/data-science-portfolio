USE [dbWork]
GO

/****** Object:  Table [dbo].[Explotacion]    Script Date: 4/14/2026 7:41:21 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Explotacion](
	[Nombre] [nvarchar](255) NULL,
	[Apellido] [nvarchar](255) NULL,
	[Edad] [float] NULL,
	[Producto] [nvarchar](255) NULL,
	[Categoria] [nvarchar](255) NULL,
	[Cantidad] [float] NULL,
	[Precio] [float] NULL,
	[Ciudad] [nvarchar](255) NULL,
	[CanalVenta] [nvarchar](255) NULL,
	[MetodoPago] [nvarchar](255) NULL,
	[Descuento] [float] NULL,
	[Costo] [float] NULL,
	[Fecha] [datetime] NULL
) ON [PRIMARY]
GO

