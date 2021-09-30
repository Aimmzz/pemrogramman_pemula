<!doctype html>
<?php include "koneksi.php"; ?>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>X-shop</title>
    <!-- Boostrap CSS-->
    <link rel="stylesheet" href="css/bootstrap.min.css" >
    <!-- Boostrap Icon CSS-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
  </head>
  <body>
    <header>
	<!-- Navbar -->
      <nav class="navbar navbar-expand-md navbar-dark bg-primary">
        <div class="container-fluid">
          <a class="navbar-brand" href="/">X-shop</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </nav>
    </header>
    <br>
    <h1></h1>
	<!-- Container -->
    <div class="container-fluid">
      <!-- Table -->
      <table class="table table-striped">
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modaltambah">
        <i class="bi-plus-lg"></i>  Tambahkan data
        </button>
        <!-- Modal Tambah-->
        <div class="modal fade" id="modaltambah" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="staticBackdropLabel">Tambahkan data</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
			  <!-- Form Tambah -->
                <form method="POST" action="tambah.php">
                  <div class="mb-3">
                    <label for="a" class="col-form-label">Nama:</label>
                    <input type="text" class="form-control" name="n" id="a">
                  </div>
                  <div class="mb-3">
                    <label for="b" class="col-form-label">Ukuran</label>
                    <select class="form-select form-select-sm" id="b" name="u">
                      <option value="S" selected>S</option>
                      <option value="M">M</option>
                      <option value="L">L</option>
                      <option value="XL">XL</option>
                    </select>
                  </div>
                  <div class="mb-3">
                    <label for="c" class="col-form-label">Warna</label>
                    <input type="text" class="form-control" name="w" id="c">
                  </div>
                  <div class="mb-3">
                    <label for="d" class="col-form-label">Stok</label>
                    <input type="number" class="form-control" name="s" id="d">
                  </div>
              </div>
              <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
              <button type="submit" class="btn btn-primary" >Simpan</button>
              </form>
              </div>
            </div>
          </div>
        </div>
        <thead>
          <tr>
            <th scope="col">ID Baju </th>
            <th scope="col">Nama</th>
            <th scope="col">Ukuran</th>
            <th scope="col">Warna</th>
            <th scope="col">Stok</th>
            <th scope="col" width="10%">Aksi</th>
          </tr>
        </thead>
        <tbody>
          <?php 
		  //Ambil semua data dari tbl_baju lalu ditampilkan melalui Loop WHILE, 1x loop = 1 baris
            $baju=mysqli_query($koneksi_db,"SELECT * FROM tbl_baju");
            while($row = mysqli_fetch_array($baju)){
             ?>
          <tr>
            <th><?php echo $row['id_baju'];?></th>
            <td><?php echo $row['nama'];?></td>
            <td><?php echo $row['ukuran'];?></td>
            <td><?php echo $row['warna'];?></td>
            <td><?php echo $row['stok'];?></td>
            <td>
			<!-- Button Aksi -->
              <a class="btn btn-danger" href="hapus.php?id=<?php echo $row['id_baju'];?>" onclick="return confirm('Yakin ingin menghapus?')"><i class="bi-trash"></i></a>
              <a class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#modaledit<?php echo $row['id_baju']; //Tiap 1 baris data, ada 1 modal edit, jadi untuk membedakannya pakai id_baju ?>"><i class="bi-pencil-square"></i></a>
              <!-- Modal Edit-->
              <div class="modal fade" id="modaledit<?php echo $row['id_baju']; //ini target modalnya ?>" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title" id="staticBackdropLabel">Tambahkan data</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
					<!-- Form Edit -->
                      <form method="POST" action="edit.php">
                        <div class="mb-3">
                          <input type="hidden" name="id" value="<?php echo $row['id_baju']; //ID Buat Edit nya ?>">
                          <label for="a" class="col-form-label">Nama:</label>
                          <input type="text" class="form-control" name="n" id="a" value="<?php echo $row['nama'];?>">
                        </div>
                        <div class="mb-3">
                          <label for="b" class="col-form-label">Ukuran</label>
                          <select class="form-select form-select-sm" id="b" name="u" value="<?php echo $row['ukuran'];?>" >
                            <option value="S">S</option>
                            <option value="M">M</option>
                            <option value="L">L</option>
                            <option value="XL">XL</option>
                          </select>
                        </div>
                        <div class="mb-3">
                          <label for="c" class="col-form-label">Warna</label>
                          <input type="text" class="form-control" name="w" id="c" value="<?php echo $row['warna'];?>">
                        </div>
                        <div class="mb-3">
                          <label for="d" class="col-form-label">Stok</label>
                          <input type="number" class="form-control" name="s" id="d" value="<?php echo $row['stok'];?>">
                        </div>
                    </div>
                    <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                    <button type="submit" class="btn btn-primary" >Simpan</button>
                    </form>
                    </div>
                  </div>
                </div>
              </div>
            </td>
          </tr>
          <?php } // tutupnya looping while ?>
        </tbody>
      </table>
      <!-- Boostrap JS-->
      <script src="js/bootstrap.bundle.min.js"></script>
    </div>
  </body>
</html>