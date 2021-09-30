<?php  
require 'function.php';
require 'cek.php';
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Barang Keluar</title>
        <link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
        <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/js/all.min.js" crossorigin="anonymous"></script>
    </head>
    <body class="sb-nav-fixed">
        <nav class="sb-topnav navbar navbar-expand navbar-dark bg-dark">
            <!-- Navbar Brand-->
            <a class="navbar-brand ps-3" href="index.php">Informasi toko</a>
            <!-- Sidebar Toggle-->
            <button class="btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0" id="sidebarToggle" href="#!"><i class="fas fa-bars"></i></button>
        
        
        </nav>
        <div id="layoutSidenav">
            <div id="layoutSidenav_nav">
                <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
                    <div class="sb-sidenav-menu">
                        <div class="nav">
                            
                        <a class="nav-link" href="index.php">
                                <div class="sb-nav-link-icon"><i class="fas fa-tachometer-alt"></i></div>
                                Stok Barang
                            </a>
                            <a class="nav-link" href="masuk.php">
                                <div class="sb-nav-link-icon"><i class="fas fa-tachometer-alt"></i></div>
                                Barang Masuk
                            </a>
                            <a class="nav-link" href="keluar.php">
                                <div class="sb-nav-link-icon"><i class="fas fa-tachometer-alt"></i></div>
                                Barang Keluar
                            </a>
                            <a class="nav-link" href="logout.php">
                                Logout
                            </a>

                            
                        </div>
                    </div>
                    <div class="sb-sidenav-footer">
                        <div class="small">Logged in as:</div>
                        Start Bootstrap
                    </div>
                </nav>
            </div>
            <div id="layoutSidenav_content">
                <main>
                    <div class="container-fluid px-4">
                        <h1 class="mt-4">Barang Keluar</h1>
                        <ol class="breadcrumb mb-4">
                            <li class="breadcrumb-item active">Dashboard</li>
                        </ol>
                    
                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                        Tambah Barang
                        </button>
                        <div class="card-body">
                                <table id="datatablesSimple">
                                    <thead>
                                        <tr>
                                            <th>No</th>
                                            <th>Nama Barang</th>
                                            <th>Deskripsi</th>
                                            <th>Penerima</th>
                                            <th>Aksi</th>

                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                        <?php
                                        $ambilsemuadatastok = mysqli_query($conn,"select * from keluar k, stok s where s.id_barang = k.id_barang");
                                        while($data=mysqli_fetch_array($ambilsemuadatastok)){
                                            $idk = $data['id_keluar'];
                                            $idb = $data['id_barang'];
                                            $tanggal = $data['tanggal'];
                                            $nama_barang = $data['nama_barang'];
                                            $qty = $data['qty'];
                                            $penerima = $data['penerima'];

                                        ?>
                                        <tr>
                                            <td><?=$tanggal;?></td>
                                            <td><?=$nama_barang;?></td>
                                            <td><?=$qty;?></td>
                                            <td><?=$penerima;?></td>
                                            <td>
                                                <button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#edit<?=$idk;?>">
                                                Edit
                                                </button>
                                                <input type="hidden" nama="id_barangygmaudihapus" value="<?=$idb;?>">
                                                <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#delete<?=$idk;?>">
                                                Delete
                                                </button>
                                            </td>
                                        </tr>




                                         <!-- update Modal -->
                                         <div class="modal fade" id="edit<?=$idk;?>">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title" id="exampleModalLabel">Edit Barang</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>
                                            <form method="post">
                                            <div class="modal-body">
                                                <input type="text" name="penerima" value="<?=$penerima;?>" class="form-control" required>
                                                <br>
                                                <input type="number" name="qty" value="<?=$qty;?>" class="form-control" required>
                                                <br>
                                                <input type="hidden" name="idb" value="<?=$idb;?>">
                                                <input type="hidden" name="idk" value="<?=$idk;?>">
                                                <button type="submit" class="btn btn-primary" name="updatebarangkeluar">Submit</button>
                                            </div>
                                            </form>
                                            </div>
                                            </div>
                                        </div>
                                        <!-- Hapus Modal -->
                                        <div class="modal fade" id="delete<?=$idk;?>">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title" id="exampleModalLabel">Hapus Barang</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>
                                            <form method="post">
                                            <div class="modal-body">
                                            Apakah Anda yakin ingin menghapus<?=$nama_barang;?>?
                                            <input type="hidden" name="idb" value="<?=$idb;?>">
                                            <input type="hidden" name="qty" value="<?=$qty;?>">
                                            <input type="hidden" name="idk" value="<?=$idk;?>">
                                            <br> 
                                            <br>
                                                <button type="submit" class="btn btn-danger" name="hapusbarangkeluar">Hapus</button>
                                            </div>
                                            </form>
                                            </div>
                                            </div>
                                        </div>
                                        
                                        
                                        <?php
                                        };   
                                        ?>
                                        </tr>
                                        
                                    </tbody>
                                </table>
                            </div>
                    </div>
                </main>
                <footer class="py-4 bg-light mt-auto">
                    <div class="container-fluid px-4">
                        <div class="d-flex align-items-center justify-content-between small">
                            <div class="text-muted">Copyright &copy; Your Website 2021</div>
                            <div>
                                <a href="#">Privacy Policy</a>
                                &middot;
                                <a href="#">Terms &amp; Conditions</a>
                            </div>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
        <script src="js/scripts.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js" crossorigin="anonymous"></script>
        <script src="assets/demo/chart-area-demo.js"></script>
        <script src="assets/demo/chart-bar-demo.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest" crossorigin="anonymous"></script>
        <script src="js/datatables-simple-demo.js"></script>
    </body>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Tambah Barang Keluar</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <form method="post">
        <div class="modal-body">
        <select name="barangnya" class="form-control">
            <?php 
            $ambilsemuadatanya = mysqli_query($conn,"select * from stok");
            while ($fetcharray = mysqli_fetch_array($ambilsemuadatanya)){
                $namabarangnya = $fetcharray['nama_barang'];
                $idbarangnya = $fetcharray['id_barang'];

                ?>
                <option value="<?=$idbarangnya;?>"><?=$namabarangnya;?></option>
                <?php
            }
            ?>
            </select>
            <br>
            <input type="number" name="qty" class="form-control" placeholder="Quantity" required>
            <br>
            <input type="text" name="penerima" placeholder="penerima" class="form-control" required>
            <br>
            <button type="submit" class="btn btn-primary" name="addbarangkeluar">Submit</button>
        </div>
        <form>
        
        </div>
    </div>
    </div>
</html>
