# Linux Command Line

## Change ownership
```
sudo chown root:llei file.txt
```

## Change Read/Write permission
### 6 = read and write
### 4 = read
```
sudo chmod 664 file.txt
```

## Info about installed pkgs
```
apt-cache policy gimp
```

## List regular and long listing
```
ls or l
ls -l
```

## Nano
```
sudo nano ./
sudo nano ./file.txt
```

## Remove directory, bypassing approval prompts
```
rm -rf mydir
```

## Repeat
```
!!
```

## Switch user
```
sudo su
su llei
```

## Updating and upgrading pkgs
```
sudo apt-get update
sudo apt-get dist-upgrade
```