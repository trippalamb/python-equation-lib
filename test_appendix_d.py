"""
Unit Tests for Appendix D: Equations Module

This test file contains unit tests for all functions in the appendix_d module.
Tests verify correctness using known values and mathematical properties.
"""

import unittest
import math
from appendix_d import (
    # Utility functions
    vector_magnitude, vector_normalize, vector_dot, vector_cross,
    vector_subtract, vector_add, matrix_multiply, matrix_vector_multiply,
    matrix_transpose, vector_scale, sign,

    # D.1 Rotational State Transformations
    D_1_1_1_roll_rotation_matrix, D_1_1_2_pitch_rotation_matrix,
    D_1_1_3_yaw_rotation_matrix, D_1_1_4_1_composite_dcm,
    D_1_1_4_2_expanded_dcm, D_1_2_1_quaternion_to_euler,
    D_1_2_2_euler_to_quaternion, D_1_2_3_quaternion_to_body_direction,

    # D.2 Spatial State Transformations
    D_2_0_1_earth_angular_velocity_vector, D_2_0_2_earth_rotation_angle,
    D_2_0_3_transport_velocity, D_2_0_4_relative_velocity_eci,
    D_2_0_5_coriolis_acceleration, D_2_0_6_centripetal_acceleration,
    D_2_0_7_relative_acceleration_eci, D_2_1_1_1_eci_to_ecr_dcm,
    D_2_1_1_2_eci_to_ecr_position, D_2_1_1_3_eci_to_ecr_velocity,
    D_2_1_1_4_eci_to_ecr_acceleration, D_2_1_2_1_eci_to_body_cg_dcm,
    D_2_1_2_2_eci_to_body_cg_position, D_2_1_2_3_eci_to_body_cg_velocity,
    D_2_1_2_3_eci_to_body_cg_acceleration, D_2_2_1_1_ecr_to_eci_dcm,
    D_2_2_1_2_ecr_to_eci_position, D_2_2_1_3_ecr_to_eci_velocity,
    D_2_2_1_4_ecr_to_eci_acceleration, D_2_2_2_ecr_to_lla,
    D_2_2_3_1_ecr_to_enu_dcm, D_2_2_3_2_ecr_to_enu_position,
    D_2_2_3_3_ecr_to_enu_velocity, D_2_2_3_3_ecr_to_enu_acceleration,
    D_2_3_1_1_enu_to_ecr_dcm, D_2_3_1_2_enu_to_ecr_position,
    D_2_3_1_3_enu_to_ecr_velocity, D_2_3_1_3_enu_to_ecr_acceleration,
    D_2_3_2_1_enu_to_ned_dcm, D_2_3_2_2_enu_to_ned_position,
    D_2_3_2_2_enu_to_ned_velocity, D_2_3_2_2_enu_to_ned_acceleration,
    D_2_4_1_1_ned_to_enu_dcm, D_2_4_1_2_ned_to_enu_position,
    D_2_4_1_2_ned_to_enu_velocity, D_2_4_1_2_ned_to_enu_acceleration,
    D_2_5_1_1_lla_to_ecr_position, D_2_6_1_1_body_cg_to_eci_dcm,
    D_2_6_1_3_body_cg_to_eci_velocity, D_2_6_1_3_body_cg_to_eci_acceleration,
    D_2_6_2_1_body_cg_to_body_nose_position, D_2_6_2_2_body_cg_to_body_nose_velocity,
    D_2_6_2_2_body_cg_to_body_nose_acceleration, D_2_7_1_1_body_nose_to_body_cg_position,
    D_2_7_1_2_body_nose_to_body_cg_velocity, D_2_7_1_2_body_nose_to_body_cg_acceleration,

    # D.3 Flight Data
    D_3_1_1_airspeed_eci, D_3_1_2_airspeed_body_cg,
    D_3_2_1_total_angle_of_attack, D_3_2_2_pitch_angle_of_attack,
    D_3_2_3_yaw_angle_of_attack,
    D_3_3_1_flight_path_angle_ecr, D_3_3_2_inertial_flight_path_angle,
    D_3_4_1_lateral_angular_rate_magnitude, D_3_4_2_precession_angle,
    D_3_4_3_precession_rate, D_3_4_4_spin_angle, D_3_4_5_spin_rate,
    D_3_5_speed_of_sound, D_3_5_mach_number,
    D_3_6_1_sensed_acceleration_eci, D_3_6_2_sensed_acceleration_body_cg,
    D_3_6_3_lateral_sensed_acceleration,

    # D.4 Aerodynamic Coefficients
    D_4_1_dynamic_pressure, D_4_2_reference_area,
    D_4_3_axial_force_coefficient, D_4_4_normal_force_coefficient,
    D_4_5_lift_coefficient,

    # D.5 Mass Properties
    D_5_1_1_inertia_tensor,

    # D.6 Propulsion
    D_6_1_thrust_magnitude,

    # D.7 Geodesy
    D_7_1_1_vincenty_ground_range, D_7_1_2_ground_range_traveled,
    D_7_2_prime_vertical_radius, D_7_3_geoid_correction_term,

    # D.8 Unit Conversions
    D_8_1_radians_to_degrees, D_8_2_degrees_to_radians,
    D_8_3_meters_to_kilometers,

    # Constants
    GAMMA_AIR, R_AIR, OMEGA_EARTH, WGS84_A, WGS84_B, WGS84_F, WGS84_E_SQ,
)


class TestUtilityFunctions(unittest.TestCase):
    """Tests for utility functions."""

    def test_vector_magnitude(self):
        """Test vector magnitude calculation."""
        self.assertAlmostEqual(vector_magnitude([3, 4, 0]), 5.0)
        self.assertAlmostEqual(vector_magnitude([1, 0, 0]), 1.0)
        self.assertAlmostEqual(vector_magnitude([0, 0, 0]), 0.0)
        self.assertAlmostEqual(vector_magnitude([1, 1, 1]), math.sqrt(3))

    def test_vector_normalize(self):
        """Test vector normalization."""
        result = vector_normalize([3, 0, 0])
        self.assertAlmostEqual(result[0], 1.0)
        self.assertAlmostEqual(result[1], 0.0)
        self.assertAlmostEqual(result[2], 0.0)

        # Normalized vector should have magnitude 1
        v = [1, 2, 3]
        normalized = vector_normalize(v)
        self.assertAlmostEqual(vector_magnitude(normalized), 1.0)

        # Zero vector
        zero_result = vector_normalize([0, 0, 0])
        self.assertEqual(zero_result, [0.0, 0.0, 0.0])

    def test_vector_dot(self):
        """Test dot product."""
        self.assertAlmostEqual(vector_dot([1, 0, 0], [0, 1, 0]), 0.0)
        self.assertAlmostEqual(vector_dot([1, 2, 3], [4, 5, 6]), 32.0)
        self.assertAlmostEqual(vector_dot([1, 0, 0], [1, 0, 0]), 1.0)

    def test_vector_cross(self):
        """Test cross product."""
        # i x j = k
        result = vector_cross([1, 0, 0], [0, 1, 0])
        self.assertAlmostEqual(result[0], 0.0)
        self.assertAlmostEqual(result[1], 0.0)
        self.assertAlmostEqual(result[2], 1.0)

        # j x i = -k
        result = vector_cross([0, 1, 0], [1, 0, 0])
        self.assertAlmostEqual(result[2], -1.0)

    def test_vector_subtract(self):
        """Test vector subtraction."""
        result = vector_subtract([5, 6, 7], [1, 2, 3])
        self.assertEqual(result, [4, 4, 4])

    def test_vector_add(self):
        """Test vector addition."""
        result = vector_add([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [5, 7, 9])

    def test_matrix_multiply(self):
        """Test 3x3 matrix multiplication."""
        I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # A * I = A
        result = matrix_multiply(A, I)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(result[i][j], A[i][j])

    def test_matrix_vector_multiply(self):
        """Test matrix-vector multiplication."""
        I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        v = [1, 2, 3]
        result = matrix_vector_multiply(I, v)
        self.assertEqual(result, [1, 2, 3])

    def test_matrix_transpose(self):
        """Test matrix transpose."""
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        A_T = matrix_transpose(A)
        self.assertEqual(A_T[0][1], A[1][0])
        self.assertEqual(A_T[2][0], A[0][2])

    def test_vector_scale(self):
        """Test vector scaling."""
        result = vector_scale([1, 2, 3], 2.0)
        self.assertEqual(result, [2, 4, 6])

    def test_sign(self):
        """Test sign function."""
        self.assertEqual(sign(5), 1.0)
        self.assertEqual(sign(-5), -1.0)
        self.assertEqual(sign(0), 0.0)


class TestD1RotationalStateTransformations(unittest.TestCase):
    """Tests for D.1 Rotational State Transformations."""

    def test_D_1_1_1_roll_rotation_matrix(self):
        """Test roll rotation matrix."""
        # Zero rotation should be identity
        R = D_1_1_1_roll_rotation_matrix(0)
        self.assertAlmostEqual(R[0][0], 1.0)
        self.assertAlmostEqual(R[1][1], 1.0)
        self.assertAlmostEqual(R[2][2], 1.0)

        # 90 degree rotation
        R = D_1_1_1_roll_rotation_matrix(math.pi / 2)
        # x stays same, y -> z, z -> -y
        self.assertAlmostEqual(R[0][0], 1.0)
        self.assertAlmostEqual(R[1][2], 1.0, places=5)
        self.assertAlmostEqual(R[2][1], -1.0, places=5)

    def test_D_1_1_2_pitch_rotation_matrix(self):
        """Test pitch rotation matrix."""
        R = D_1_1_2_pitch_rotation_matrix(0)
        self.assertAlmostEqual(R[1][1], 1.0)

    def test_D_1_1_3_yaw_rotation_matrix(self):
        """Test yaw rotation matrix."""
        R = D_1_1_3_yaw_rotation_matrix(0)
        self.assertAlmostEqual(R[2][2], 1.0)

    def test_D_1_1_4_composite_vs_expanded(self):
        """Test that composite and expanded DCM give same result."""
        phi, theta, psi = 0.1, 0.2, 0.3

        dcm_composite = D_1_1_4_1_composite_dcm(phi, theta, psi)
        dcm_expanded = D_1_1_4_2_expanded_dcm(phi, theta, psi)

        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(dcm_composite[i][j], dcm_expanded[i][j], places=10)

    def test_D_1_2_quaternion_euler_roundtrip(self):
        """Test quaternion to Euler and back."""
        phi, theta, psi = 0.1, 0.2, 0.3

        q_s, q_i, q_j, q_k = D_1_2_2_euler_to_quaternion(phi, theta, psi)
        phi2, theta2, psi2 = D_1_2_1_quaternion_to_euler(q_s, q_i, q_j, q_k)

        self.assertAlmostEqual(phi, phi2, places=10)
        self.assertAlmostEqual(theta, theta2, places=10)
        self.assertAlmostEqual(psi, psi2, places=10)

    def test_D_1_2_2_euler_to_quaternion_unit(self):
        """Test that quaternion from Euler angles has unit magnitude."""
        phi, theta, psi = 0.5, 0.3, 0.7
        q_s, q_i, q_j, q_k = D_1_2_2_euler_to_quaternion(phi, theta, psi)

        mag = math.sqrt(q_s**2 + q_i**2 + q_j**2 + q_k**2)
        self.assertAlmostEqual(mag, 1.0, places=10)

    def test_D_1_2_3_quaternion_to_body_direction(self):
        """Test quaternion to body direction."""
        # Identity quaternion (no rotation)
        x_body = D_1_2_3_quaternion_to_body_direction(1.0, 0.0, 0.0, 0.0)
        self.assertAlmostEqual(x_body[0], 1.0)
        self.assertAlmostEqual(x_body[1], 0.0)
        self.assertAlmostEqual(x_body[2], 0.0)


class TestD2SpatialStateTransformations(unittest.TestCase):
    """Tests for D.2 Spatial State Transformations."""

    def test_D_2_0_1_earth_angular_velocity_vector(self):
        """Test Earth angular velocity vector."""
        omega = D_2_0_1_earth_angular_velocity_vector()
        self.assertEqual(omega[0], 0.0)
        self.assertEqual(omega[1], 0.0)
        self.assertAlmostEqual(omega[2], OMEGA_EARTH)

    def test_D_2_0_2_earth_rotation_angle(self):
        """Test Earth rotation angle."""
        # After 1 day, should rotate ~2*pi radians
        t = 86400.0  # seconds in a day
        angle = D_2_0_2_earth_rotation_angle(t)
        self.assertAlmostEqual(angle, OMEGA_EARTH * t)

    def test_D_2_0_3_transport_velocity(self):
        """Test transport velocity."""
        # At equator, transport velocity is largest
        r_eci = [WGS84_A, 0, 0]  # On equator
        v_transport = D_2_0_3_transport_velocity(r_eci)

        # Should be in y direction (omega x r for r in x gives y)
        self.assertAlmostEqual(v_transport[0], 0.0, places=5)
        self.assertGreater(v_transport[1], 0)
        self.assertAlmostEqual(v_transport[2], 0.0)

    def test_D_2_1_1_eci_to_ecr_roundtrip(self):
        """Test ECI to ECR and back."""
        psi = 0.5
        r_eci = [1e6, 2e6, 3e6]

        R_eci_to_ecr = D_2_1_1_1_eci_to_ecr_dcm(psi)
        r_ecr = D_2_1_1_2_eci_to_ecr_position(R_eci_to_ecr, r_eci)

        R_ecr_to_eci = D_2_2_1_1_ecr_to_eci_dcm(psi)
        r_eci_back = D_2_2_1_2_ecr_to_eci_position(R_ecr_to_eci, r_ecr)

        for i in range(3):
            self.assertAlmostEqual(r_eci[i], r_eci_back[i], places=5)

    def test_D_2_2_2_ecr_to_lla_known_point(self):
        """Test ECR to LLA conversion at known point."""
        # Point on equator at prime meridian at surface
        lat, lon, alt = 0.0, 0.0, 0.0
        r_ecr = D_2_5_1_1_lla_to_ecr_position(lat, lon, alt)

        lat2, lon2, alt2 = D_2_2_2_ecr_to_lla(r_ecr)

        self.assertAlmostEqual(lat2, lat, places=6)
        self.assertAlmostEqual(lon2, lon, places=6)
        self.assertAlmostEqual(alt2, alt, delta=1.0)  # Within 1 meter

    def test_D_2_2_2_ecr_to_lla_pole(self):
        """Test ECR to LLA at north pole."""
        lat, lon, alt = math.pi / 2, 0.0, 0.0
        r_ecr = D_2_5_1_1_lla_to_ecr_position(lat, lon, alt)

        lat2, lon2, alt2 = D_2_2_2_ecr_to_lla(r_ecr)

        self.assertAlmostEqual(lat2, lat, places=5)
        self.assertAlmostEqual(alt2, alt, delta=1.0)

    def test_D_2_2_3_ecr_to_enu_dcm_orthogonal(self):
        """Test that ECR to ENU DCM is orthogonal."""
        lat, lon = 0.5, 1.0
        R = D_2_2_3_1_ecr_to_enu_dcm(lat, lon)
        R_T = matrix_transpose(R)

        # R * R^T should be identity
        I = matrix_multiply(R, R_T)
        for i in range(3):
            for j in range(3):
                expected = 1.0 if i == j else 0.0
                self.assertAlmostEqual(I[i][j], expected, places=10)

    def test_D_2_3_enu_to_ecr_roundtrip(self):
        """Test ENU to ECR position roundtrip."""
        lat, lon, alt = 0.5, 1.0, 1000.0
        r_enu = [100, 200, 50]

        R_enu_to_ecr = D_2_3_1_1_enu_to_ecr_dcm(lat, lon)
        r_pv = D_7_2_prime_vertical_radius(WGS84_A, WGS84_E_SQ, lat)
        z_geoid = D_7_3_geoid_correction_term(WGS84_E_SQ, r_pv, lat)

        r_ecr = D_2_3_1_2_enu_to_ecr_position(R_enu_to_ecr, r_enu, r_pv, alt, z_geoid)

        R_ecr_to_enu = D_2_2_3_1_ecr_to_enu_dcm(lat, lon)
        r_enu_back = D_2_2_3_2_ecr_to_enu_position(R_ecr_to_enu, r_ecr, z_geoid, r_pv, alt)

        for i in range(3):
            self.assertAlmostEqual(r_enu[i], r_enu_back[i], places=3)

    def test_D_2_3_2_enu_to_ned_dcm(self):
        """Test ENU to NED DCM."""
        R = D_2_3_2_1_enu_to_ned_dcm()
        self.assertEqual(R[0][1], 1)  # North = North
        self.assertEqual(R[1][0], 1)  # East = East
        self.assertEqual(R[2][2], -1)  # Down = -Up

    def test_D_2_3_2_enu_ned_roundtrip(self):
        """Test ENU to NED roundtrip."""
        r_enu = [100, 200, 300]

        r_ned = D_2_3_2_2_enu_to_ned_position(r_enu)
        r_enu_back = D_2_4_1_2_ned_to_enu_position(r_ned)

        for i in range(3):
            self.assertAlmostEqual(r_enu[i], r_enu_back[i])

    def test_D_2_5_1_1_lla_to_ecr_equator(self):
        """Test LLA to ECR at equator."""
        lat, lon, alt = 0.0, 0.0, 0.0
        r_ecr = D_2_5_1_1_lla_to_ecr_position(lat, lon, alt)

        # On equator at prime meridian, should be (r_a, 0, 0) approximately
        self.assertAlmostEqual(r_ecr[0], WGS84_A, delta=1.0)
        self.assertAlmostEqual(r_ecr[1], 0.0, delta=1.0)
        self.assertAlmostEqual(r_ecr[2], 0.0, delta=1.0)

    def test_D_2_6_body_cg_to_eci_roundtrip(self):
        """Test Body CG to ECI roundtrip."""
        phi, theta, psi = 0.1, 0.2, 0.3
        v_body = [100, 50, 25]

        R_body_to_eci = D_2_6_1_1_body_cg_to_eci_dcm(phi, theta, psi)
        v_eci = D_2_6_1_3_body_cg_to_eci_velocity(R_body_to_eci, v_body)

        R_eci_to_body = D_2_1_2_1_eci_to_body_cg_dcm(phi, theta, psi)
        v_body_back = D_2_1_2_3_eci_to_body_cg_velocity(R_eci_to_body, v_eci)

        for i in range(3):
            self.assertAlmostEqual(v_body[i], v_body_back[i], places=10)

    def test_D_2_6_2_body_cg_nose_roundtrip(self):
        """Test Body CG to Body Nose roundtrip."""
        r_body_cg = [10, 5, 2]
        r_cg = [1.5, 0, 0]

        r_nose = D_2_6_2_1_body_cg_to_body_nose_position(r_body_cg, r_cg)
        r_cg_back = D_2_7_1_1_body_nose_to_body_cg_position(r_nose, r_cg)

        for i in range(3):
            self.assertAlmostEqual(r_body_cg[i], r_cg_back[i])


class TestD3FlightData(unittest.TestCase):
    """Tests for D.3 Flight Data."""

    def test_D_3_1_1_airspeed_eci(self):
        """Test ECI airspeed calculation."""
        v_rel = [100, 200, 300]
        v_wind = [10, 20, 30]
        v_air = D_3_1_1_airspeed_eci(v_rel, v_wind)

        self.assertEqual(v_air, [90, 180, 270])

    def test_D_3_2_1_total_angle_of_attack_zero(self):
        """Test total angle of attack with aligned flow."""
        # Flow directly along x-axis
        v_air = [100, 0, 0]
        aoa = D_3_2_1_total_angle_of_attack(v_air)
        self.assertAlmostEqual(aoa, 0.0)

    def test_D_3_2_1_total_angle_of_attack_90deg(self):
        """Test total angle of attack at 90 degrees."""
        v_air = [0, 100, 0]
        aoa = D_3_2_1_total_angle_of_attack(v_air)
        self.assertAlmostEqual(aoa, math.pi / 2)

    def test_D_3_2_2_pitch_angle_of_attack(self):
        """Test pitch angle of attack."""
        # 45 degree pitch up
        v_air = [100, 0, 100]
        aoa = D_3_2_2_pitch_angle_of_attack(v_air)
        self.assertAlmostEqual(aoa, math.pi / 4)

    def test_D_3_2_3_yaw_angle_of_attack(self):
        """Test yaw angle of attack."""
        v_air = [100, 100, 0]
        aoa = D_3_2_3_yaw_angle_of_attack(v_air)
        self.assertAlmostEqual(aoa, math.pi / 4)

    def test_D_3_3_1_flight_path_angle_ecr_climbing(self):
        """Test flight path angle for climbing trajectory."""
        # Velocity vector pointing up and forward at equator
        v_ecr = [100, 0, 100]  # 45 degree climb
        lat, lon = 0.0, 0.0
        fpa = D_3_3_1_flight_path_angle_ecr(v_ecr, lat, lon)
        self.assertAlmostEqual(fpa, math.pi/4, places=5)

    def test_D_3_3_1_flight_path_angle_ecr_level(self):
        """Test flight path angle for level flight."""
        # Velocity tangent to surface at equator
        v_ecr = [0, 100, 0]  # East
        lat, lon = 0.0, 0.0
        fpa = D_3_3_1_flight_path_angle_ecr(v_ecr, lat, lon)
        self.assertAlmostEqual(fpa, 0.0, places=5)

    def test_D_3_4_1_lateral_angular_rate_magnitude(self):
        """Test lateral angular rate magnitude."""
        omega_q = 3.0
        omega_r = 4.0
        omega_s = D_3_4_1_lateral_angular_rate_magnitude(omega_q, omega_r)
        self.assertAlmostEqual(omega_s, 5.0)

    def test_D_3_4_4_spin_angle_wrap(self):
        """Test spin angle wrapping."""
        # Start at 0, accumulate 3*pi should wrap to -pi + epsilon
        phi = D_3_4_4_spin_angle(0, 3 * math.pi)
        self.assertTrue(-math.pi <= phi <= math.pi)

    def test_D_3_4_5_spin_rate(self):
        """Test spin rate equals roll rate."""
        omega_p = 2.5
        spin_rate = D_3_4_5_spin_rate(omega_p)
        self.assertEqual(spin_rate, omega_p)

    def test_D_3_5_speed_of_sound(self):
        """Test speed of sound at standard temp."""
        T = 288.15  # Standard sea level temp in K
        v_sound = D_3_5_speed_of_sound(T)
        # Should be approximately 340 m/s
        self.assertAlmostEqual(v_sound, 340.3, delta=1.0)

    def test_D_3_5_mach_number(self):
        """Test Mach number calculation."""
        T = 288.15
        v_sound = D_3_5_speed_of_sound(T)
        v_air = [v_sound, 0, 0]  # Mach 1

        mach = D_3_5_mach_number(v_air, T)
        self.assertAlmostEqual(mach, 1.0, places=5)

    def test_D_3_6_1_sensed_acceleration_eci(self):
        """Test sensed acceleration in ECI."""
        a_eci = [10, 20, 30]
        a_gravity = [0, 0, -9.81]

        a_sensed = D_3_6_1_sensed_acceleration_eci(a_eci, a_gravity)
        self.assertAlmostEqual(a_sensed[2], 30 + 9.81)

    def test_D_3_6_3_lateral_sensed_acceleration(self):
        """Test lateral sensed acceleration."""
        a_sensed = [10, 3, 4]  # 3-4-5 triangle in y-z
        a_lateral = D_3_6_3_lateral_sensed_acceleration(a_sensed)
        self.assertAlmostEqual(a_lateral, 5.0)

    def test_D_3_1_2_airspeed_body_cg(self):
        """Test airspeed transformation to body frame."""
        # Identity rotation (no rotation)
        R = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        v_air_eci = [100, 50, 25]
        v_air_body = D_3_1_2_airspeed_body_cg(R, v_air_eci)
        self.assertEqual(v_air_body, v_air_eci)

    def test_D_3_3_2_inertial_flight_path_angle(self):
        """Test inertial flight path angle."""
        # Velocity directly radial outward at equator
        v_eci = [100, 0, 0]
        lat_eci, lon_eci = 0.0, 0.0
        fpa = D_3_3_2_inertial_flight_path_angle(v_eci, lat_eci, lon_eci)
        self.assertAlmostEqual(fpa, math.pi / 2, places=5)

    def test_D_3_6_2_sensed_acceleration_body_cg(self):
        """Test sensed acceleration transformation to body frame."""
        R = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        a_sensed_eci = [1, 2, 3]
        a_sensed_body = D_3_6_2_sensed_acceleration_body_cg(R, a_sensed_eci)
        self.assertEqual(a_sensed_body, a_sensed_eci)


class TestD4AerodynamicCoefficients(unittest.TestCase):
    """Tests for D.4 Aerodynamic Coefficients."""

    def test_D_4_1_dynamic_pressure(self):
        """Test dynamic pressure calculation."""
        rho = 1.225  # kg/m^3
        v = [100, 0, 0]  # 100 m/s

        P = D_4_1_dynamic_pressure(rho, v)
        expected = 0.5 * rho * 100**2
        self.assertAlmostEqual(P, expected)

    def test_D_4_2_reference_area(self):
        """Test reference area calculation."""
        m = 1000  # kg
        C_b = 500  # kg/m^2
        C_D = 0.5

        S_ref = D_4_2_reference_area(m, C_b, C_D)
        self.assertAlmostEqual(S_ref, m / (C_b * C_D))

    def test_D_4_3_axial_force_coefficient(self):
        """Test axial force coefficient."""
        F_x = 1000
        P_dyn = 10000
        S_ref = 1.0

        C_a = D_4_3_axial_force_coefficient(F_x, P_dyn, S_ref)
        self.assertAlmostEqual(C_a, 0.1)

    def test_D_4_5_lift_coefficient(self):
        """Test lift coefficient calculation."""
        aoa = 0.0  # Zero angle of attack
        C_a = 0.1
        C_n = 0.5

        C_L = D_4_5_lift_coefficient(aoa, C_a, C_n)
        # At zero AOA: C_L = -sin(0)*C_a + cos(0)*C_n = C_n
        self.assertAlmostEqual(C_L, C_n)


class TestD5MassProperties(unittest.TestCase):
    """Tests for D.5 Mass Properties."""

    def test_D_5_1_1_inertia_tensor_symmetric(self):
        """Test that inertia tensor is symmetric."""
        I = D_5_1_1_inertia_tensor(100, 200, 300, 10, 20, 30)

        self.assertEqual(I[0][1], I[1][0])
        self.assertEqual(I[0][2], I[2][0])
        self.assertEqual(I[1][2], I[2][1])


class TestD6Propulsion(unittest.TestCase):
    """Tests for D.6 Propulsion."""

    def test_D_6_1_thrust_magnitude(self):
        """Test thrust magnitude calculation."""
        Fx, Fy, Fz = 3000, 4000, 0
        thrust = D_6_1_thrust_magnitude(Fx, Fy, Fz)
        self.assertAlmostEqual(thrust, 5000.0)


class TestD7Geodesy(unittest.TestCase):
    """Tests for D.7 Geodesy."""

    def test_D_7_1_1_vincenty_coincident_points(self):
        """Test Vincenty with coincident points."""
        d = D_7_1_1_vincenty_ground_range(0, 0, 0, 0)
        self.assertEqual(d, 0.0)

    def test_D_7_1_1_vincenty_known_distance(self):
        """Test Vincenty with known distance."""
        # London to Paris approximately 344 km
        lat1 = math.radians(51.5074)  # London
        lon1 = math.radians(-0.1278)
        lat2 = math.radians(48.8566)  # Paris
        lon2 = math.radians(2.3522)

        d = D_7_1_1_vincenty_ground_range(lat1, lon1, lat2, lon2)
        # Should be approximately 344 km
        self.assertAlmostEqual(d / 1000, 344, delta=5)

    def test_D_7_1_2_ground_range_traveled(self):
        """Test ground range traveled."""
        points = [
            (0.0, 0.0, 0.0),
            (0.0, 0.001, 0.0),
            (0.0, 0.002, 0.0),
        ]

        total = D_7_1_2_ground_range_traveled(points)
        self.assertGreater(total, 0)

    def test_D_7_2_prime_vertical_radius(self):
        """Test prime vertical radius at equator."""
        r_pv = D_7_2_prime_vertical_radius(WGS84_A, WGS84_E_SQ, 0.0)
        # At equator, should equal semi-major axis
        self.assertAlmostEqual(r_pv, WGS84_A)

    def test_D_7_3_geoid_correction_term(self):
        """Test geoid correction at equator is zero."""
        r_pv = D_7_2_prime_vertical_radius(WGS84_A, WGS84_E_SQ, 0.0)
        z_geoid = D_7_3_geoid_correction_term(WGS84_E_SQ, r_pv, 0.0)
        self.assertAlmostEqual(z_geoid, 0.0)


class TestConstants(unittest.TestCase):
    """Tests for module constants."""

    def test_wgs84_constants_consistency(self):
        """Test WGS84 constant relationships."""
        # b = a * (1 - f)
        expected_b = WGS84_A * (1 - WGS84_F)
        self.assertAlmostEqual(WGS84_B, expected_b)

        # e^2 = 2f - f^2
        expected_e_sq = 2 * WGS84_F - WGS84_F**2
        self.assertAlmostEqual(WGS84_E_SQ, expected_e_sq)

    def test_wgs84_a_value(self):
        """Test WGS84 semi-major axis value."""
        self.assertEqual(WGS84_A, 6378137.0)

    def test_omega_earth_value(self):
        """Test Earth angular velocity value."""
        self.assertAlmostEqual(OMEGA_EARTH, 7.292115e-5)

    def test_gamma_air_value(self):
        """Test specific heat ratio for air."""
        self.assertEqual(GAMMA_AIR, 1.4)


class TestD8UnitConversions(unittest.TestCase):
    """Tests for D.8 Unit Conversions."""

    def test_D_8_1_radians_to_degrees(self):
        """Test radians to degrees conversion."""
        deg = D_8_1_radians_to_degrees(math.pi)
        self.assertAlmostEqual(deg, 180.0)

    def test_D_8_2_degrees_to_radians(self):
        """Test degrees to radians conversion."""
        rad = D_8_2_degrees_to_radians(180.0)
        self.assertAlmostEqual(rad, math.pi)

    def test_D_8_conversion_roundtrip(self):
        """Test radians to degrees roundtrip."""
        rad_orig = 1.5
        deg = D_8_1_radians_to_degrees(rad_orig)
        rad_back = D_8_2_degrees_to_radians(deg)
        self.assertAlmostEqual(rad_orig, rad_back)

    def test_D_8_3_meters_to_kilometers(self):
        """Test meters to kilometers conversion."""
        km = D_8_3_meters_to_kilometers(1500)
        self.assertAlmostEqual(km, 1.5)


if __name__ == '__main__':
    unittest.main()
