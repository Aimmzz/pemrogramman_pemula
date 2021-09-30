<?php
session_start();
// membuat koneksi ke database
$conn = mysqli_connect("localhost", "root", "", "informasi_toko");

//coba koneksi
//if($conn) {
//echo 'berhasil';
//}


//INSERT stok
if (isset($_POST['addnewbarang']))
{
    $nama_barang = $_POST['nama_barang'];
    $deskripsi = $_POST['deskripsi'];
    $stok = $_POST['stok'];

    $addtotable = mysqli_query($conn, "insert into stok (nama_barang, deskripsi, stok) values ('$nama_barang','$deskripsi','$stok')");
    if ($addtotable)
    {
        header('loction:index.php');
    }
    else
    {
        echo 'Gagal';
    }
}
//UPDATE stok
if (isset($_POST['updatebarang']))
{
    $idb = $_POST['idb'];
    $nama_barang = $_POST['nama_barang'];
    $deskripsi = $_POST['deskripsi'];

    $update = mysqli_query($conn, "update stok set nama_barang='$nama_barang', deskripsi='$deskripsi' where id_barang ='$idb'");
    if ($update)
    {
        header('location:index.php');
    }
    else
    {
        echo 'Gagal';
    }
}
//DELETE stok
if (isset($_POST['hapusbarang']))
{
    $idb = $_POST['idb'];

    $hapus = mysqli_query($conn, "delete from stok where id_barang='$idb'");
    if ($hapus)
    {
        header('location:index.php');
    }
    else
    {
        echo 'Gagal';
    }
}

//INSERT masuk
if (isset($_POST['barangmasuk']))
{
    $barangnya = $_POST['barangnya'];
    $penerima = $_POST['penerima'];
    $qty = $_POST['qty'];

    $cekstoksekarang = mysqli_query($conn, "select * from stok where id_barang ='$barangnya'");
    $ambildatanya = mysqli_fetch_array($cekstoksekarang);

    $stoksekarang = $ambildatanya['stok'];
    $tambahkanstoksekarangdenganquantity = $stoksekarang + $qty;

    
    $addtomasuk = mysqli_query($conn, "insert into masuk (id_barang, keterangan, qty) values('$barangnya','$penerima','$qty')");
    $updatestokmasuk = mysqli_query($conn, "update stok set stok='$tambahkanstoksekarangdenganquantity' where id_barang='$barangnya'");
    if ($addtomasuk && $updatestokmasuk)
    {
        header('location:masuk.php');
    }
    else
    {
        echo 'Gagal';
    }
}

//UPDATE masuk
if (isset($_POST['updatebarangmasuk']))
{
    $idb = $_POST['idb'];
    $idm = $_POST['idm'];
    $deskripsi = $_POST['keterangan'];
    $qty = $_POST['qty'];

    $lihatstok = mysqli_query($conn, "select * from stok where id_barang='$idb'");
    $stoknya = mysqli_fetch_array($lihatstok);
    $stokskrg = $stoknya['stok'];
	
    $qtyskrg = mysqli_query($conn, "select *from masuk where id_masuk='$idm'");
    $qtynya = mysqli_fetch_array($qtyskrg);
    $qtyskrg = $qtynya['qty'];
    if ($qty > $qtyskrg)
    {
        $selisih = $qty - $qtyskrg;
        $kurangin = $stokskrg + $selisih;
        $kurangistoknya = mysqli_query($conn, "update stok set stok='$kurangin' where id_barang='$idb'");
        $updatenya = mysqli_query($conn, "update masuk set qty='$qty', keterangan='$deskripsi' where id_masuk='$idm'");
        if ($kurangistoknya && $updatenya)
        {
            header('location:masuk.php');
        }
        else
        {
            echo 'Gagal';
        }
    }
    else
    { //masih ada yg error soalnya gak berubah padahal udah di ganti di browsernya
        $selisih = $qtyskrg - $qty;
        $kurangin = $stokskrg - $selisih;
        $kurangistoknya = mysqli_query($conn, "update stok set stok='$kurangin' where id_barang='$idb'");
        $updatenya = mysqli_query($conn, "update masuk set qty='$qty', keterangan='$deskripsi' where id_masuk='$idm'");
        if ($kurangistoknya && $updatenya)
        {
            header('location:masuk.php');
        }
        else
        {
            echo 'Gagal';
        }
    }

}

//DELETE masuk
if (isset($_POST['hapusbarangmasuk']))
{
    $idb = $_POST['idb'];
    $qty = $_POST['qty'];
    $idm = $_POST['idm'];

    $getdatastok = mysqli_query($conn, "select * from stok where id_barang='$idb'");
    $data = mysqli_fetch_array($getdatastok);
    $stok = $data['stok'];

    $selisih = $stok - $qty;

    $update = mysqli_query($conn, "update stok set stok='$selisih' where id_barang='$idb'");
    $hapusdata = mysqli_query($conn, "delete from masuk where id_masuk='$idm'");

    if ($update && $hapusdata)
    {
        header('location:masuk.php');
    }
    else
    {
        header('location:masuk.php');
    }
}

//INSERT keluar
if (isset($_POST['addbarangkeluar']))
{
    $barangnya = $_POST['barangnya'];
    $penerima = $_POST['penerima'];
    $qty = $_POST['qty'];

    $cekstoksekarang = mysqli_query($conn, "select * from stok where id_barang ='$barangnya'");
    $ambildatanya = mysqli_fetch_array($cekstoksekarang);

    $stoksekarang = $ambildatanya['stok'];
    $tambahkanstoksekarangdenganquantity = $stoksekarang - $qty;

    $addtokeluar = mysqli_query($conn, "insert into keluar (id_barang, penerima, qty) values('$barangnya','$penerima',$qty)");
    $updatestokkeluar = mysqli_query($conn, "update stok set stok='$tambahkanstoksekarangdenganquantity' where id_barang='$barangnya'");
    if ($addtokeluar && $updatestokkeluar)
    {
        header('location:keluar.php');
    }
    else
    {
        echo 'Gagal';
    }
}

//UPDATE keluar
if (isset($_POST['updatebarangkeluar']))
{
    $idb = $_POST['idb'];
    $idk = $_POST['idk'];
    $penerima = $_POST['penerima'];
    $qty = $_POST['qty'];

    $lihatstok = mysqli_query($conn, "select * from stok where id_barang='$idb'");
    $stoknya = mysqli_fetch_array($lihatstok);
    $stokskrg = $stoknya['stok'];

    $qtyskrg = mysqli_query($conn, "select *from keluar where id_keluar='$idk'");
    $qtynya = mysqli_fetch_array($qtyskrg);
    $qtyskrg = $qtynya['qty'];
    if ($qty > $qtyskrg)
    {
        $selisih = $qtyskrg - $qty;
        $kurangin = $stokskrg + $selisih;
        $kurangistoknya = mysqli_query($conn, "update stok set stok='$kurangin' where id_barang='$idb'");
        $updatenya = mysqli_query($conn, "update keluar set qty='$qty', penerima='$penerima' where id_keluar='$idk'");
        if ($kurangistoknya && $updatenya)
        {
            header('location:keluar.php');
        }
        else
        {
            echo 'Gagal';
        }
    }
    else
    {
        $selisih = $qtyskrg - $qty;
        $kurangin = $stokskrg + $selisih;
        $kurangistoknya = mysqli_query($conn, "update stok set stok='$kurangin' where id_barang='$idb'");
        $updatenya = mysqli_query($conn, "update keluar set qty='$qty', penerima='$penerima' where id_keluar='$idk'");
        if ($kurangistoknya && $updatenya)
        {
            header('location:keluar.php');
        }
        else
        {
            echo 'Gagal';
        }
    }

}

//DELETE keluar
if (isset($_POST['hapusbarangkeluar']))
{
    $idb = $_POST['idb'];
    $qty = $_POST['qty'];
    $idk = $_POST['idk'];

    $getdatastok = mysqli_query($conn, "select * from stok where id_barang='$idb'");
    $data = mysqli_fetch_array($getdatastok);
    $stok = $data['stok'];

    $selisih = $stok + $qty;

    $update = mysqli_query($conn, "update stok set stok='$selisih' where id_barang='$idb'");
    $hapusdata = mysqli_query($conn, "delete from keluar where id_keluar='$idk'");

    if ($update && $hapusdata)
    {
        header('location:keluar.php');
    }
    else
    {
        header('location:keluar.php');
    }
}

?>
