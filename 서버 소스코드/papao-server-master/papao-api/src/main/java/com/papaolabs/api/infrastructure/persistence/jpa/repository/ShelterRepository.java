package com.papaolabs.api.infrastructure.persistence.jpa.repository;

import com.papaolabs.api.infrastructure.persistence.jpa.entity.Shelter;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ShelterRepository extends JpaRepository<Shelter, Long> {
    Shelter findByShelterCode(Long shelterCode);
    List<Shelter> findBySidoCodeAndGunguCode(Long sidoCode, Long gunguCode);
}
